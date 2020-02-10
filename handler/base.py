from state_machine.base import StateMachine


class Handler:
    def could_handle(self, sm: StateMachine):
        raise Exception("Not implemented")

    @staticmethod
    def handle(self, sm):
        raise Exception("Not implemented")
