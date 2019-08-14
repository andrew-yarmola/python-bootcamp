from flask import Flask
import os
import socket
import redis

# Connect to Redis
redis_conn = redis.from_url('redis://localhost:6379')

app = Flask(__name__)

@app.route("/")
def hello():
    print("Runnnig Hello")
    try :
        visits = redis_conn.incr("counter")
    except redis.RedisError :
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Basic Visit Counter</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "Undefined"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='localhost', port=9999)
