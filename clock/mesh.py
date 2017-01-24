"""Provide nodes network knowledge."""

import websockets


class Node:
    def __init__(self, name, host, port):
        self.name = name
        self.host = host
        self.port = port

    def uri(self, path):
        return f'ws://{self.host}:{self.port}{path}'

    def connection(self, path):
        return websockets.connect(self.uri(path))


# TODO service discovery, a dictionary works in the meantime
grid = {'clock': Node('clock', 'localhost', 8765),
        'iopin': Node('iopin', 'localhost', 8765),
        'buzzer': Node('buzzer', 'localhost', 8765 + 1),
        }
