from __future__ import annotations

from ConfigParams import ConfigParams
from ConnectionManager import ConnectionManager

if __name__ == "__main__":
    # The client code.

    configParams = ConfigParams("127.0.0.1", 8080, "abc")

    # 1. Create server if not exists
    connectionManager = ConnectionManager(configParams)


