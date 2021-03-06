#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from oslo_log import log
from tempest import config

from senlin.tests.tempest import base
from senlin.tests.tempest.common import clustering_client

CONF = config.CONF
lOG = log.getLogger(__name__)


class BaseSenlinAPITest(base.BaseSenlinTest):

    network_resources = {
        'network': False,
        'router': False,
        'subnet': False,
        'dhcp': False,
    }

    @classmethod
    def setup_clients(cls):
        super(BaseSenlinAPITest, cls).setup_clients()
        cls.client = clustering_client.ClusteringAPIClient(
            cls.os.auth_provider,
            CONF.clustering.catalog_type,
            CONF.identity.region,
            **cls.os.default_params_with_timeout_values
        )
