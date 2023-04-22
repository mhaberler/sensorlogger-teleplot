
# receives sensorlogger push updates and relays to teleplot.fr

# run as:
# TELEPLOT=teleplot.fr:<destport> flask run --host=0.0.0.0 --port=<local portnumber>

# in sensorlogger, configure HTTP push as:
# http://<thisip>:<local portnumber>/data

import json
import os
import socket
from flask import Flask, request


teleplot = os.environ["TELEPLOT"] 
host,port=  teleplot.split(':')
teleplotAddr = (host, int(port))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def teleplot(msg):
     payload = msg["payload"]
     for r in payload:
          sensor = r["name"]
          if sensor == "test":
              print("got test push message")
              continue
          time = r["time"]/1000000
          for name, value  in r["values"].items():
            msg = f"{sensor}.{name}:{time}:{value}|np"
            # print(msg)
            sock.sendto(msg.encode(), teleplotAddr)

                 
app = Flask(__name__)

@app.route("/data", methods=["POST"])
def data():  # listens to the data streamed from the sensor logger
    if str(request.method) == "POST":
        data = json.loads(request.data)
        teleplot(data)
    return "success"

