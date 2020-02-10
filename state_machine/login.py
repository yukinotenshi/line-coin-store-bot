from state_machine.LINE import LineStateMachine
from handler.login import HANDLERS
import time


class LoginStateMachine(LineStateMachine):
    def __init__(self):
        super().__init__()
        self.handlers = HANDLERS
        self.cleaner = lambda x: time.sleep(10)
