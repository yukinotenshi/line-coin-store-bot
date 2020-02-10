class StateMachine:
    def __init__(self):
        self.handlers = []
        self.data = {}
        self.state = ""
        self.cleaner = None

    def pick_handler(self):
        for h in self.handlers:
            try:
                if h.could_handle(self):
                    print(h)
                    return h
            except Exception as e:
                print(e)
                continue

        return None

    def execute(self):
        while self.state != "DONE":
            handler = self.pick_handler()
            if handler is None:
                break
            try:
                handler.handle(self)
            except Exception as e:
                print(e)

            if self.cleaner:
                self.cleaner(self)
