from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def __str__(self):
        return f'from Client({self.sender}): {self.content}'


class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        print("Detaching: ", observer)
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ServerSubject(Subject):
    _state: int = None
    messages = []

    clients: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Server: Attached a client. ", observer)
        self.clients.append(observer)

    def detach(self, observer: Observer) -> None:
        self.clients.remove(observer)

    def notify(self) -> None:
        print("Server: Notifying clients...")
        for observer in self.clients:
            if observer.id != self.messages[-1].sender:
                print(f"Client({observer.id}) received message from client {self.messages[-1].sender}")
                observer.update(self)

    def send_message(self, message) -> None:

        print(f"Client({message.sender}) sent message {message.content}")
        self.messages.append(message)

        # print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    id = 0

    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class ClientObserver(Observer):
    def __init__(self, clientId, ip_address, port, key):
        self.id = clientId
        self.ip_address = ip_address
        self.port = port
        self.key = key

    def update(self, subject: Subject) -> None:
        print(f"Client ({self.id}): updated")
