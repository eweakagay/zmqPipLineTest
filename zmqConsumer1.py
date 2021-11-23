#ch1
import zmq
import json

from zmq.sugar import socket

ctx=zmq.Context()
sockPULL=ctx.socket(zmq.PULL)
sockPULL.connect("tcp://127.0.0.1:5556")
sockPUSH=ctx.socket(zmq.PUSH)
sockPUSH.connect("tcp://127.0.0.1:5557")
while True:
    i=0
    msg=sockPULL.recv_json()
    print("ch1:recved"+msg["msg"])
    Json=json.dumps({"id":i,"msg":msg["msg"]})
    sockPUSH.send_json(Json)
    i=i+1
