# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.apps.clock.app import Clock


class TestClockTestAllItemsPresentNewAlarm(GaiaMtbfTestCase):

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)

        self.clock = Clock(self.marionette)
        self.app_id = self.launch_by_touch("Clock")

    def test_all_items_present_new_alarm(self):
        # Wait for the new alarm screen to load

        new_alarm = self.clock.tap_new_alarm()

        # Ensure label has the default placeholder and text
        self.assertEquals(new_alarm.alarm_label_placeholder, 'Alarm name')

        # Ensure repeat has the default value
        self.assertEquals(new_alarm.alarm_repeat, 'Never')

        # Ensure sound has the default value
        self.assertEquals(new_alarm.alarm_sound, 'Classic Buzz')

        # Ensure snooze has the default value
        self.assertEquals(new_alarm.alarm_snooze, '5 minutes')
        
        # Close the new Alarm setting
        self.marionette.find_element("id", "alarm-close").tap()
        
