import os

from command import Command


class ChangeDirectory(Command):
    def __init__(self, shell):
        super().__init__("cd", shell)

    def execute(self, *args, **kwargs):
        if len(args) != 1:
            print(f"Error: expected exactly 1 path, got {len(args)}.")
            return

        path = args[0]
        os.chdir(path)


class Clear(Command):
    def __init__(self, shell):
        super().__init__("clear", shell)

    def execute(self, *args, **kwargs):
        print("\033[2J\033[H", end="")


class Exit(Command):
    def __init__(self, shell):
        super().__init__("exit", shell)

    def execute(self, *args, **kwargs):
        self.shell.stop()


class Export(Command):
    def __init__(self, shell):
        super().__init__("export", shell)

    def execute(self, *args, **kwargs):
        print(args)


class List(Command):
    def __init__(self, shell):
        super().__init__("list", shell)

    def execute(self, *args, **kwargs):
        if len(args) == 0:
            path = os.getcwd()
        else:
            path = args[0]

        if not os.path.exists(path):
            print(f"Error: path '{path}' does not exist.")
            return

        if os.path.isdir(path):
            for item in os.listdir(path):
                print(item)
        else:
            print(path)


class PrintEnv(Command):
    def __init__(self, shell):
        super().__init__("env", shell)

    def execute(self, *args, **kwargs):
        print(self.shell.env)


class Speak(Command):
    def __init__(self, shell):
        super().__init__("speak", shell)

    def execute(self, *args, **kwargs):
        if len(args) == 0:
            return
        for text in args:
            print(text)
