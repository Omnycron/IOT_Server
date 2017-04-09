#!usr/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for
from flask_cors import CORS
import time
import sys
import reading
import datastore
import logging
import json

logging.basicConfig(filename="api.log", level=logging.DEBUG)

app = Flask(__name__)
CORS(app)

@app.errorhandler(404)
def not_found(self):
    return make_response(jsonify({"error": "Not found"}), 404)
    
@app.route("/weather/api/v1.0/readings", methods=["GET"])
def get_readings():
    return make_response(str(datastore.getreadings(30)), 200)

@app.route("/weather/api/v1.0/readings/<int:reading_id>", methods=["GET"])
def get_single_reading(reading_id):
    return make_response(str(datastore.getsinglereading(reading_id)), 200)

@app.route("/weather/api/v1.0/readings/", methods=["POST"])
def create_reading():
    try:
        print ("POST")
        print request
        req_json = request.get_json()
        print req_json    
        
        req_json["id"] = None
        req_json["timestamp"] = None
        
        ourReading = reading.Reading(req_json)
        print ourReading
        insertrresult = datastore.insertreading(ourReading)
        
        if insertrresult:
            return jsonify({"status": "succeeded"}), 200
        else:
            return jsonify({"status": "failed"}), 400
    except Exception as e:
        print "data not inserted"
        print e
    return "OK"
        
if __name__=="__main__":
    print "starting server..."
#    app.run(host="0.0.0.0")
    app.run(host="0.0.0.0", debug=True)
