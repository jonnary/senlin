# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from tempest.lib import decorators

from senlin.tests.tempest.api import base


class TestPolicyTypeList(base.BaseSenlinAPITest):

    @decorators.idempotent_id('72cc0347-3eab-4cf6-b1ee-531b11f20550')
    def test_policy_type_list(self):
        res = self.client.list_objs('policy-types')

        # Verify resp of policy type list API
        self.assertEqual(200, res['status'])
        self.assertIsNotNone(res['body'])
        policy_types = res['body']
        for policy_type in policy_types:
            self.assertIn('name', policy_type)
