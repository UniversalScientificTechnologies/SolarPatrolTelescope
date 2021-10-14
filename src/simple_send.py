import zmq
import time

print("Connecting to hello Patrola server…")
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://arom-patrola.asu.cas.cz:5555")

while 1:
    socket.send_string("move;0;-10")
    print("send")
    time.sleep(4)
