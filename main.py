from __future__ import annotations

from ConnectionManager import ConnectionManager
from patterns import ServerSubject, ClientObserver, Message


class ConfigParams:
    def __init__(self, ip_address, port, key):
        self.ip_address = ip_address
        self.port = port
        self.key = key


if __name__ == "__main__":
    # The client code.

    configParams = ConfigParams("127.0.0.1", 8080, "abc")

    # 1. Create server if not exists
    connectionManager = ConnectionManager(configParams)

    # 2. Bind subject to server
    #subject = ServerSubject()

    # 3. If client key is accepted, attach client to subject (server)
    #observer_a = ClientObserver(1, "127.0.0.1", 8080, "abc")
    #observer_b = ClientObserver(2, "127.0.0.1", 8080, "abc")
    #observer_c = ClientObserver(3, "127.0.0.1", 8080, "dec")
    #subject.attach(observer_a)
    #subject.attach(observer_b)
    #subject.attach(observer_c)

    #subject.send_message(message=Message(observer_a.id, "Hola Cliente A"))
    #subject.send_message(message=Message(observer_b.id, "Hola Cliente B"))

    # subject.detach(observer_a)

    # subject.send_message("Hola desde cliente A")
