from flask import Flask
from redis import Redis, RedisError
import os, socket

# Connect to Redis server
redis = Redis(host="redis-server", db=0, socket_timeout=2, socket_connect_timeout=10)

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1> Hello! </h1>"

# Count the number of visits with Redis database.
@app.route("visit")
def visit_count():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<p> Cannot connect to Redis </p>"
    html = f"<h1> Number of visits: {visits}</h1></br></br>Hostname: {socket.gethostname()}"

if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")