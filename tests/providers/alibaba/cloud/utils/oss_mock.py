#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
import json

from airflow.models import Connection

OSS_PROJECT_ID_HOOK_UNIT_TEST = 'example-project'


def mock_oss_hook_default_project_id(self, oss_conn_id='mock_oss_default', region='mock_region'):
    self.oss_conn_id = oss_conn_id
    self.oss_conn = Connection(
        extra=json.dumps(
            {
                'auth_type': 'AK',
                'access_key_id': 'mock_access_key_id',
                'access_key_secret': 'mock_access_key_secret',
            }
        )
    )
    self.region = region
