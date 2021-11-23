#mother:rep

import zmq

ctx=zmq.Context()
sock=ctx.socket(zmq.REP)
sock.bind("tcp://*:5555")

sock.recv_string()
print("recved.")
msg="hello!"
print("sended:"+msg)
sock.send_string(msg)

sock.close()
#fin
