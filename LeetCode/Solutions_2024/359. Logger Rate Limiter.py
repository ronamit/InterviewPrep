class Logger:

    def __init__(self):
        self.last_prints = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        should_print = False
        if message in self.last_prints:
            last_time = self.last_prints[message]
            should_print = timestamp >= last_time + 10
        else:
            should_print = True
        if should_print:
            self.last_prints[message] = timestamp
        return should_print


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
