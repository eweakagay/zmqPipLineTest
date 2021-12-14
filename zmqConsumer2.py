#ch2
import zmq
import json

from zmq.sugar import socket

ctx=zmq.Context()
sockPULL=ctx.socket(zmq.PULL)
sockPULL.connect("tcp://127.0.0.1:5556")
sockPUSH=ctx.socket(zmq.PUSH)
sockPUSH.connect("tcp://127.0.0.1:5557")

msg=sockPULL.recv_json()
print("ch2:recved"+msg["msg"])
Json=json.dumps({"id":"2","msg":msg["msg"]})
sockPUSH.send_json(Json)
