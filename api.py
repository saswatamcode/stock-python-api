from datetime import date
from nsepy import get_history
from flask import Flask, redirect, url_for, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import json
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

CORS(app)

class stockdata(Resource):
    def post(self):
        req = request.get_json()
        data = get_history(symbol=req["symbol"], start=date(req["startyear"],req["startmonth"],req["startday"]), end=date(req["endyear"],req["endmonth"],req["endday"]))
        out = data.to_json(orient='records')
        dd = json.loads(out)
        print(data[['Close']])
        print(out)
        return dd,200

api.add_resource(stockdata, '/stock')
        
if __name__ == '__main__':
   app.run(debug = True)
