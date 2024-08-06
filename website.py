from flask import Flask, request, jsonify
import json
app = Flask(__name__)

info = []

@app.errorhandler(404)
def page_not_found(e):
    return json.loads('{"Status": "ERROR"}')

def check(number):
    if number > len(info) or number == 0:
        return False
    return True

@app.route('/', methods = ["GET"])
def main():
    return json.loads('{"Info": "Main page", "Status": "OK"}')

@app.route('/save', methods = ["POST"])
def save():
    data = request.json["Info"]
    print (data)
    info.append(data)
    return json.loads('{"Info": "Data saved", "Status": "OK"}')

@app.route('/read/<int:number>', methods = ["GET"])
def read(number):
    if check(number):
        return jsonify({"Info": info[number-1], "Status": "OK"})
    else:
        return json.loads('{"Info": "No data on this key", "Status": "ERROR"}')

@app.route('/delete/<int:number>', methods = ["GET"])
def delete(number):
    if check(number):
        info.remove(info[number-1])
        return json.loads('{"Info": "Cell ' + str(number) +' data removed", "Status": "OK"}')
    else:
        return json.loads('{"Info": "This data does not exist", "Status": "ERROR"}')

@app.route('/readall', methods = ["GET"])
def readall():
    if len(info) > 0:
        return jsonify({"Info": info, "Status": "OK"})
    return json.loads('{"Info": "No data exist", "Status": "ERROR"}')

@app.route('/deleteall', methods = ["GET"])
def deleteall():
    global info
    if len(info) != 0:
        info = []
        return json.loads('{"Info": "All data deleted", "Status": "OK"}')
    return json.loads('{"Info": "No data was recorded", "Status": "ERROR"}')

if __name__ == '__main__':
   app.run(debug = True)