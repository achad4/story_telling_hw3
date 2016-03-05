import flask
import redis
import collections
import json
import numpy as np

app = flask.Flask(__name__)
conn = redis.Redis()

def histogram_data():
    keys = conn.keys()
    values = conn.mget(keys)
    c = collections.Counter(values)
    z = sum(c.values())
    #data represents the distribution of rentals at different stations
    return {k:v/float(z) for k,v in c.items()}

@app.route("/histogram")
def histogram():
    return json.dumps(histogram_data())


@app.route("/entropy")
def entropy():
    distribution = histogram_data()
    entropy = 0
    for n in distribution.values():
        entropy = np.log(n)
    return json.dumps({ "entropy" : -entropy })

@app.route("/rate")
def moving_avg_stream_rate():
    avg_rate = conn.get("movingAvgRate")
    if avg_rate:
        return json.dumps({"rate" : avg_rate})
    else:
        return json.dumps({"rate" : 0})

if __name__ == "__main__":
    app.debug = True
    app.run()