from requests import post
from . import constants as c


class ADOConnector(object):
    def __init__(self, organization, project, personal_access_token, team=None, issue_type="task"):
        self.auth = ('', personal_access_token)
        self.team = f"{project}"
        if team:
            self.team = f"{project}\\{team}"
        self.url = c.CREATE_ISSUE_URL.format(organization=organization, project=project,
                                             type=issue_type, rules="false", notify="false")
        self.query_url = "https://dev.azure.com/{organization}/{project}/{team}/" \
                         "_apis/wit/wiql?api-version=5.1".format(organization=organization, team=team,
                                                                 project=project)

    def create_finding(self, title, description=None, priority=None,
                       assignee=None, issue_hash=None, custom_fields=None):
        if not custom_fields:
            custom_fields = dict()
        body = []
        if title:
            title_piece = c.TITLE
            title_piece['value'] = title
            body.append(title_piece)
        if description:
            description_piece = c.DESCRIPTION
            description_piece['value'] = description
            body.append(description_piece)
        if priority:
            priority_piece = c.PRIORITY
            priority_piece['value'] = c.PRIORITY_MAPPING[priority]
            body.append(priority_piece)
        if assignee:
            assignee_piece = c.ASSIGNED_TO
            assignee_piece['value'] = assignee
            body.append(assignee_piece)
        team_piece = c.TEAM
        team_piece['value'] = self.team
        body.append(team_piece)
        iteration_piece = c.ITERATION
        iteration_piece['value'] = self.team
        body.append(iteration_piece)
        for each in custom_fields:
            _piece = {"op": "add", "path": each, "from": None, "value": custom_fields[each]}
            body.append(_piece)
        if not self.search_for_issue(issue_hash):
            return post(self.url, auth=self.auth, json=body,
                        headers={'content-type': 'application/json-patch+json'}).content
        else:
            return {}

    def search_for_issue(self, issue_hash=None):
        q = f"SELECT [System.Id] From WorkItems Where [System.Description] Contains \"{issue_hash}\""
        data = post(self.query_url, auth=self.auth, json={"query": q},
                    headers={'content-type': 'application/json'}).json()
        if len(data["workItems"]):
            return True
        return False
