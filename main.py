from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

from ConnectionManager import ConnectionManager


class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def __str__(self):
        return f'from Client({self.sender}): {self.content}'


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class ServerSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: int = None
    messages = []
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    clients: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer. ", observer)
        self.clients.append(observer)

    def detach(self, observer: Observer) -> None:
        self.clients.remove(observer)

    """
    Send message to all clients that are not this id
    """

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self.clients:
            if observer.id != self.messages[-1].sender:
                print("Sending message to client ", observer.id)
                observer.update(self)

    def send_message(self, message) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nServer: Sending message...", message.__str__())
        self.messages.append(message)
        self._state = randrange(0, 10)

        #print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """
    id = 0

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass



"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""


class ClientObserver(Observer):
    def __init__(self, clientId, ip_address, port, key):
        self.id = clientId
        self.ip_address = ip_address
        self.port = port
        self.key = key

    def update(self, subject: Subject) -> None:
        print("Client A: New state: ", subject._state)


class ConfigParams:
    def __init__(self, ip_address, port, key):
        self.ip_address = ip_address
        self.port = port
        self.key = key

if __name__ == "__main__":
    # The client code.

    configParams = ConfigParams("127.0.0.1", 8080, "abc")

    #1. Create server if not exists
    connectionManager = ConnectionManager(configParams)
    #connectionManager.createServer()

    #2. Bind subject to server
    subject = ServerSubject()

    #3. If client key is accepted, attach client to subject (server)
    observer_a = ClientObserver(1, "127.0.0.1", 8080, "abc")
    observer_b = ClientObserver(2, "127.0.0.1", 8080, "abc")
    observer_c = ClientObserver(3, "127.0.0.1", 8080, "dec")

    subject.attach(observer_a)
    subject.attach(observer_b)
    subject.attach(observer_c)

    subject.send_message(message=Message(observer_a.id, "Hola Cliente A"))
    subject.send_message(message=Message(observer_b.id, "Hola Cliente B"))

    # subject.detach(observer_a)

    # subject.send_message("Hola desde cliente A")
