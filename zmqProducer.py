#producer:req->push
import zmq
import time
import json

ctx=zmq.Context()
sockRECV=ctx.socket(zmq.REQ)
sockRECV.connect("tcp://127.0.0.1:5555")#ch1:5556 ch2:5558
sockPUSH=ctx.socket(zmq.PUSH)
sockPUSH.connect("tcp://127.0.0.1:5556")

sockRECV.send_string("ewe")
msgRow="iwiu"
msgRow=sockRECV.recv_string()
print("original:"+msgRow)
msg1={"msg":msgRow[0:int(len(msgRow)/2)]}
json1=json.dumps(msg1)
print("send msg1:"+msg1["msg"])
sockPUSH.send_json(json1)

time.sleep(0.1)
msg2={"msg":msgRow[int(len(msgRow)/2):]}
json2=json.dumps(msg2)
print("send msg2:"+msg2["msg"])
sockPUSH.send_json(json2)
