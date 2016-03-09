import flask
import redis
import collections
import json
import numpy as np
from flask.ext.cors import CORS, cross_origin

app = flask.Flask(__name__)
CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
conn = redis.Redis()

# @app.after_request
# def after_request(response):
#   print "yoo"
#   response.headers.add('Access-Control-Allow-Origin', '*')
#   response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#   response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
#   return response


def histogram_data():
    keys = conn.keys()
    values = []
    for key in keys:
        try:
            r = conn.hget(key, "stationName")
            values.append(r)
        except Exception as e:
            continue
    c = collections.Counter(values)
    z = sum(c.values())
    #data represents the distribution of rentals at different stations
    return {k:v/float(z) for k,v in c.items()}

@app.route("/histogram")
@cross_origin()
def histogram():
    response = flask.json.jsonify(histogram_data())
    # resp.headers['Access-Control-Allow-Origin'] = 'x-requested-with'
    return response

@app.route("/probability")
def probability_of_rental_from_station():
    stationName = request.args.get('stationName', '')
    distribution = histogram()
    return flask.json.jsonify({ "probability" : distribution['stationName'] })

@app.route("/entropy")
def entropy():
    distribution = histogram_data()
    entropy = 0
    for n in distribution.values():
        entropy = np.log(n)
    return flask.json.jsonify({ "entropy" : -entropy })

@app.route("/rate")
def moving_avg_stream_rate():
    avg_rate = conn.get("movingAvgRate")
    if avg_rate:
        return flask.json.jsonify({"rate" : avg_rate})
    else:
        return flask.json.jsonify({"rate" : 0})

if __name__ == "__main__":
    app.debug = True
    app.run()