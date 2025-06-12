import os

from command import Command


class ChangeDirectory(Command):
    def __init__(self):
        super().__init__("cd")

    def execute(self, *args):
        if len(args) != 1:
            print(f"Error: expected exactly 1 path, got {len(args)}.")
            return

        path = args[0]
        os.chdir(path)
