#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pandas as pd

from catalyst.data.data_portal import DataPortal

from logbook import Logger

log = Logger('DataPortalExchange')


class DataPortalExchange(DataPortal):
    def __init__(self, exchange, *args, **kwargs):
        self.exchange = exchange
        super(DataPortalExchange, self).__init__(*args, **kwargs)

    def get_history_window(self,
                           assets,
                           end_dt,
                           bar_count,
                           frequency,
                           field,
                           data_frequency,
                           ffill=True):
        return self.exchange.get_history_window(
            assets,
            end_dt,
            bar_count,
            frequency,
            field,
            data_frequency,
            ffill)

    def get_spot_value(self, assets, field, dt, data_frequency):
        return self.exchange.get_spot_value(assets, field, dt, data_frequency)

    def get_adjusted_value(self, asset, field, dt,
                           perspective_dt,
                           data_frequency,
                           spot_value=None):
        # TODO: does this pertain to cryptocurrencies?
        raise NotImplementedError("get_adjusted_value is not implemented yet!")
