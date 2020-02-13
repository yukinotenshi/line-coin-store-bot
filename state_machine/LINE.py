from state_machine.base import StateMachine
from appium import webdriver
import os
import time


class LineStateMachine(StateMachine):
    def __init__(self, driver=None):
        super().__init__()
        if not driver:
            self.data["driver"] = webdriver.Remote("http://localhost:4723/wd/hub", {
                'platformName': 'android',
                'app': os.getenv("APK_DIR"),
                'deviceName': 'emulator',
                'noReset': True,
                'fullReset': False
            })
            time.sleep(5)
        else:
            self.data['driver'] = driver

    def execute(self):
        start = time.time()
        super().execute()
        end = time.time()
        print(end-start)

    def close(self):
        self.data['driver'].quit()
