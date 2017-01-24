import sys

import sketches
from mesh import grid


def main():
    sketch = sys.argv[1]
    node = grid[sketch]
    if sketch == 'clock':
        # delegate the asynchronous execution to the event loop
        sketches.Clock().run()
    elif sketch == 'iopin':
        # arguments in the constructor go as is to our `setup` method
        sketches.IOPin().run(node.host, node.port)
    elif sketch == 'buzzer':
        sketches.Buzzer().run(node.host, node.port)
    else:
        print('unknown sketch, please choose clock, iopin or buzzer')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
