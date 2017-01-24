import random
import asyncio
import time

from factory import Looper, reactive


class Clock(Looper):

    def __init__(self, ticks=5, delay=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._delay = delay
        self._path = '/datafeed'
        self._ticks = range(ticks - 1)

    def run(self):
        # Wait until other processes wake up.
        # There is probably a better way to do this.
        time.sleep(0.5)
        asyncio.get_event_loop()\
               .run_until_complete(self.tock())

    async def tock(self):
        await self.stream('clock', self._ticks, self._path)


class IOPin(Looper):
    """Set an IO pin to 0 or 1 randomly."""

    def __init__(self, chance=0.5, sequence_len=5, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chance = chance
        self.sequence_len = sequence_len

    def state(self):
        """Toggle state, randomly."""
        return int(random.random() < self.chance)

    @reactive
    async def loop(self, channel, msg):
        """Callback on new data."""
        self.out(f'new tick triggered on {channel}: {msg}')
        bit_stream = [self.state() for _ in range(self.sequence_len)]
        self.out(f'toggling pin state: {bit_stream}')
        await self.stream('buzzer', bit_stream, channel)
        return 'acknowledged'


class Buzzer(Looper):
    """Buzz on light changes."""

    def __init__(self, sound='buzz', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sound = sound

    @reactive
    async def loop(self, channel, msg):
        """Buzzing."""
        behavior = self.sound if msg == '1' else '...'
        self.out(f'messsage {msg} received -> {behavior}')
        return behavior
