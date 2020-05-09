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


