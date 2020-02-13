from state_machine.LINE import LineStateMachine
from handler.add_friend import HANDLERS
import time


class AddFriendStateMachine(LineStateMachine):
    def __init__(self, target, driver=None):
        super().__init__(driver)
        self.handlers = HANDLERS
        self.cleaner = lambda x: time.sleep(3)
        self.data['first_time'] = True
        self.data['target'] = target
