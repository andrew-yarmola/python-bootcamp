from flask import Flask
from fakeredis import FakeStrictRedis
import os
import socket

app = Flask(__name__)
redis_client = FakeStrictRedis()

@app.route("/")
def hello():
    print("Runnnig Hello")
    try :
        visits = redis_client.incr("counter")
    except redis.RedisError :
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Basic Visit Counter</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "Undefined"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='localhost', port=9999)
