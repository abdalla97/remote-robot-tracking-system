

from flask import Flask,jsonify,request
import datetime;

app =   Flask(__name__)


@app.route('/returncoordinates', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):

        return currentJson


@app.route('/insertCoordinates', methods=['GET', 'POST'])
def insertCoordinates():
    content = request.json
    data = {
       "x":content['x'],
      "y":content['y'],
      "theta":content['theta'],
      "timestamp" : datetime.datetime.now()
        }


    global currentJson
    currentJson = jsonify(data)
    return currentJson




