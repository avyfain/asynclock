import asyncio
import time

from functools import wraps

import websockets

import mesh


class Looper:
    """ Glue components to manage the evented-loop model. """

    def __init__(self, *args, **kwargs):
        self._delay = 0
        self.grid = mesh.grid

    def out(self, text):
        print(f'[ {type(self).__name__} ] {text}')

    def run(self, host, port):
        try:
            server = websockets.serve(self.loop, host, port)
            self.out(f'serving on {host}:{port}')
            asyncio.get_event_loop().run_until_complete(server)
            asyncio.get_event_loop().run_forever()
        except OSError:
            self.out("Can't bind to port! Is the server already running?")
        except KeyboardInterrupt:
            self.out('Keyboard interruption, aborting.')
            asyncio.get_event_loop().stop()
        finally:
            asyncio.get_event_loop().close()

    def node(self, name):
        """Search for the given node in the grid."""
        return self.grid.get(name)

    async def stream(self, target, data, channel):
        self.out('starting to stream message to {}'.format(target))

        # use the node websocket connection defined in mesh.py
        async with self.node(target).connection(channel) as ws:
            for part in data:
                self.out(f'> sending payload: {part}')
                # websockets requires bytes or strings
                await ws.send(str(part))
                recvd = await ws.recv()
                self.out(f'< {recvd}')
                time.sleep(self._delay)


def reactive(fn):
    @wraps(fn)
    async def on_connection(instance, websocket, path):
        """Dispatch events and wrap execution."""
        instance.out(f'** new client connected, path={path}')
        # process messages as long as the connection is open or
        # an error is raised

        while True:
            try:
                message = await websocket.recv()
                acknowledgement = await fn(instance, path, message)
                await websocket.send(acknowledgement or 'n/a')
            except websockets.exceptions.ConnectionClosed as e:
                instance.out(f'Done processing messages: {e}\n')
                break
    return on_connection
