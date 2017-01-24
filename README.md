# Asynclock - An async experiment with "devices"

A rework of [Xavier Bruhiere](https://github.com/hackliff)'s tutorial on [Reactive Python](https://www.packtpub.com/books/content/reactive-python-%E2%80%93-asynchronous-programming-rescue-part-1)

## Usage

```
$ honcho start
21:23:58 system   | clock.1 started (pid=87076)
21:23:58 system   | pin.1 started (pid=87077)
21:23:58 system   | buzzer.1 started (pid=87078)
21:23:58 pin.1    | [ IOPin ] serving on localhost:8765
21:23:58 buzzer.1 | [ Buzzer ] serving on localhost:8766
21:23:59 clock.1  | [ Clock ] starting to stream message to clock
21:23:59 pin.1    | [ IOPin ] ** new client connected, path=/datafeed
21:23:59 clock.1  | [ Clock ] > sending payload: 0
21:23:59 pin.1    | [ IOPin ] new tick triggered on /datafeed: 0
21:23:59 pin.1    | [ IOPin ] toggling pin state: [0, 1, 1, 0, 1]
21:23:59 pin.1    | [ IOPin ] starting to stream message to buzzer
21:23:59 buzzer.1 | [ Buzzer ] ** new client connected, path=/datafeed
21:23:59 pin.1    | [ IOPin ] > sending payload: 0
21:23:59 buzzer.1 | [ Buzzer ] messsage 0 received -> ...
21:23:59 pin.1    | [ IOPin ] < ...
21:23:59 pin.1    | [ IOPin ] > sending payload: 1
21:23:59 buzzer.1 | [ Buzzer ] messsage 1 received -> buzz
21:23:59 pin.1    | [ IOPin ] < buzz
21:23:59 pin.1    | [ IOPin ] > sending payload: 1
21:23:59 buzzer.1 | [ Buzzer ] messsage 1 received -> buzz
21:23:59 pin.1    | [ IOPin ] < buzz
21:23:59 pin.1    | [ IOPin ] > sending payload: 0
21:23:59 buzzer.1 | [ Buzzer ] messsage 0 received -> ...
21:23:59 pin.1    | [ IOPin ] < ...
21:23:59 pin.1    | [ IOPin ] > sending payload: 1
21:23:59 buzzer.1 | [ Buzzer ] messsage 1 received -> buzz
21:23:59 pin.1    | [ IOPin ] < buzz
21:23:59 buzzer.1 | [ Buzzer ] Done processing messages: WebSocket connection is closed: code = 1000, no reason.
...
```