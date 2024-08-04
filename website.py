from flask import Flask, request
import json
app = Flask(__name__)

info = []

@app.errorhandler(404)
def page_not_found(e):
    return json.loads('{"info": "This page does not exist"}')

def check(number):
    if number > len(info) or number == 0:
        return False
    return True

@app.route('/', methods = ["GET"])
def main():
    return json.loads('{"info": "Main page"}')

@app.route('/save', methods = ["POST"])
def save():
    data = {"info": request.json["info"]}
    info.append(data)
    return json.loads('{"info": "Data saved"}')

@app.route('/read/<int:number>', methods = ["GET"])
def read(number):
    if check(number):
        return info[number-1]
    else:
        return json.loads('{"info": "No data on this key"}')

@app.route('/delete/<int:number>', methods = ["GET"])
def delete(number):
    if check(number):
        info.remove(info[number-1])
        return ('{"info": "Cell ' + str(number) +' data removed"}')
    else:
        return json.loads('{"info": "This data does not exist"}')

@app.route('/readall', methods = ["GET"])
def readall():
    if len(info) > 0:
        return info
    return json.loads('{"info": "No data exist"}')

@app.route('/deleteall', methods = ["GET"])
def deleteall():
    global info
    if len(info) != 0:
        info = []
        return json.loads('{"info": "All data deleted"}')
    return json.loads('{"info": "No data was recorded"}')

if __name__ == '__main__':
   app.run(debug = True)