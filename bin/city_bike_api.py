import flask
import redis
import collections
import json
import unicodedata
import re
import numpy as np
import city_bike_api
from flask.ext.cors import CORS, cross_origin

app = flask.Flask(__name__)
#this is so the server displaying the distribution can make cross domain requests
CORS(app)
conn = redis.Redis()

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
    #data represents the distribution of rentals at different stations
    return {k:v for k,v in c.items()}


@app.route("/post_alert", methods=['POST'])
def set_alert():
    message = flask.request.form['message']
    conn.set('alert', message)
    return 'OK'

@app.route("/get_alert")
def get_alert():
    alert = conn.get('alert')
    #after whatever reporting system accesses the most recent alert, it's not needed anymore
    conn.delete('alert')
    if(alert):
        return flask.json.jsonify({ "alert" : alert } )
    return flask.json.jsonify({ "alert" : None } )

@app.route("/histogram")
@cross_origin()
def histogram():
    response = flask.json.jsonify(histogram_data())
    return response

@app.route("/probability")
def probability_of_rental_from_station():
    stationName = flask.request.args.get('stationName', '')
    distribution = histogram_data()
    z = sum(distribution.values())
    return flask.json.jsonify({ "probability" : float(distribution[stationName])/z })

@app.route("/entropy")
def entropy():
    distribution = histogram_data()
    entropy = 0
    z = sum(distribution.values())
    for n in distribution.values():
        entropy = entropy + float(n)/z * np.log(float(n)/z)
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