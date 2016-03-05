import flask
import redis
import collections
import json
import numpy

app = flask.Flask(__name__)
conn = redis.Redis()

def histogramData():
    keys = conn.keys()
    values = conn.mget(keys)
    print values
    c = collections.Counter(values)
    z = sum(c.values())
    #data represents the distribution of rentals at different stations
    return {k:v/float(z) for k,v in c.items()}

@app.route("/histogramData")
def histogramJson():
    return json.dumps(histogramData())


@app.route("/entropy")
def entropy():
    distribution = histogramData()
    entropy = 0
    for p in distribution:
        print p
        entropy = entropy + p * numpy.log(p)
    return -entropy

    # return -sum([p * numpy.log(p) for p in distribution.values()]) 

if __name__ == "__main__":
    app.debug = True
    app.run()