import os

from command_registry import CommandRegistry
from parser import Parser


class Shell:
    def __init__(self, name, prompt=None, commands=CommandRegistry()):
        self.name = name
        self.running = True
        self.env = {}
        self.commands = commands
        self.parser = Parser()

        if prompt is None:
            self.env["prompt"] = lambda: f"{self.name} {os.getcwd()}\n> "
        else:
            self.env["prompt"] = prompt

    def add_command(self, c):
        self.commands.add(c)

    def run(self):
        while self.running:
            # Refresh prompt
            prompt = self.env["prompt"]()

            # Get cleaned user entry
            entry = input(prompt)

            # Parse line
            cmd_name, args = self.parser.parse(entry)

            # Get command
            cmd = self.commands.get(cmd_name)

            # Execute command if exists
            if cmd is not None:
                cmd.execute(*args)
            else:
                print(f"Error: command {cmd_name} does not exist.")

    def stop(self):
        self.running = False
