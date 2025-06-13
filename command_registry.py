class CommandRegistry:
    def __init__(self):
        self.commands = {}

    def add(self, c):
        self.commands[c.name] = c

    def get(self, cname):
        return self.commands.get(cname)
