# -*- coding: cp1252 -*-
from flask import Flask, jsonify,request
import lang

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    return "API is working fine"


@app.route('/summariser',methods=['POST'])
def summariser():
    req_data = request.get_json()
    return jsonify(lang.summariser(req_data['text']))

if __name__ == "__main__":
    #app.debug = True
    app.run(host="0.0.0.0", port="5000")