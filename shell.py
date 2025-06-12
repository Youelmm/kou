import os

from command_registry import commmand_registry


class Shell:
    def __init__(self, name, prompt=None):
        self.name = name
        if prompt is None:
            self._prompt = f"{self.name} {os.getcwd()} > "
        else:
            self._prompt = prompt

    @property
    def prompt(self):
        return f"{self.name} {os.getcwd()} > "

    def run(self):
        while True:
            entry = input(self.prompt).strip().split()
            command_name, args = entry[0], entry[1:]
            command = commmand_registry.get(command_name)
            if command is not None:
                command.execute(*args)


shell = Shell("zen")
shell.run()
