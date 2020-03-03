#!/usr/bin/python3
# coding=utf-8

#   Copyright 2019 getcarrier.io
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
    Constants
"""

PRIORITY_MAPPING = {"Critical": 1, "High": 1, "Medium": 2, "Low": 3, "Info": 4}

TITLE = {"op": "add", "path": "/fields/System.Title", "from": None, "value": ""}
PRIORITY = {"op": "add", "path": "/fields/Microsoft.VSTS.Common.Priority", "from": None, "value": 2}
DESCRIPTION = {"op": "add", "path": "/fields/System.Description", "from": None, "value": ""}
ASSIGNED_TO = {"op": "add", "path": "/fields/System.AssignedTo", "from": None, "value": ""}
TEAM = {"op": "add", "path": "/fields/System.AreaPath", "from": None, "value": ""}
ITERATION = {"op": "add", "path": "/fields/System.IterationPath", "from": None, "value": ""}
CREATE_ISSUE_URL = 'https://dev.azure.com/{organization}/{project}/_apis/wit/workitems/' \
                   '${type}?bypassRules={rules}&suppressNotifications={notify}&api-version=5.1'
