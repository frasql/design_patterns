from abc import ABCMeta, abstractmethod
from enum import Enum


State = Enum('State', 'new running sleeping restart zombie')

class Server(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self) -> None:
        pass

    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass


class FileServer(Server):
    def __init__(self) -> None:
        self.name = 'FileServer'
        self.state = State.new

    def boot(self):
        self.state = State.running

    def kill(self, restart=True):
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name, permissions):
        print(f"Trying to create file '{name}' for user {user}, with {permissions}")


class ProcessServer(Server):
    def __init__(self) -> None:
        self.name = 'FileServer'
        self.state = State.new

    def boot(self):
        self.state = State.running

    def kill(self, restart=True):
        self.state = State.restart if restart else State.zombie

    def create_process(self, user, name):
        print(f"Trying to create process '{name}' for user {user}")

class OperatingSystem:
    """ The Facade """
    

    def __init__(self) -> None:
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [i.boot for i in (self.fs, self.ps)]

    def create_file(self, user, name, permissions):
        return self.fs.create_file(user, name, permissions)

    def create_process(self, user, name):
        return self.ps.create_process(user, name)