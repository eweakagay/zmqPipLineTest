import zmq
import json

from zmq.sugar import socket

ctx=zmq.Context()
sockRECV=ctx.socket(zmq.PULL)
sockRECV.bind("tcp://127.0.0.1:5557")

text1=json.loads(sockRECV.recv_json())
print("id:"+str(text1["id"])+"msg:"+str(text1["msg"]))
text2=json.loads(sockRECV.recv_json())
print("id:"+str(text2["id"])+"msg:"+str(text2["msg"]))
