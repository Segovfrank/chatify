import os
import threading


def ConnectionManager(params):

    #1. Start server
    serverThread = ServerThread(params)
    serverThread.start()


class ServerThread(threading.Thread):
    def __init__(self, params):
        threading.Thread.__init__(self)
        self.params = params

    def run(self):
        os.system(f"python3 server.py {self.params.ip_address} {self.params.port} {self.params.key}")
