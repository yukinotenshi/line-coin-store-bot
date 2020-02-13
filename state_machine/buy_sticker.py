from state_machine.LINE import LineStateMachine
from handler.buy_sticker import HANDLERS
import time


class BuyStickerStateMachine(LineStateMachine):
    def __init__(self, sticker_name, target_id):
        super().__init__()
        self.handlers = HANDLERS
        self.cleaner = lambda x: time.sleep(3)
        self.data['first_time'] = True
        self.data['sticker_name'] = sticker_name
        self.data['target'] = target_id
