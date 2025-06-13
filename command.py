from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, name, shell):
        self.name = name
        self.shell = shell

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass
