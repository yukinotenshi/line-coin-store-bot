from state_machine.LINE import LineStateMachine
from handler.buy_sticker import HANDLERS
import time


class BuyStickerStateMachine(LineStateMachine):
    def __init__(self, sticker_link, target_id, driver=None):
        super().__init__(driver)
        self.handlers = HANDLERS
        self.cleaner = lambda x: time.sleep(3)
        self.data['first_time'] = True
        self.data['sticker_link'] = sticker_link
        self.data['target'] = target_id
