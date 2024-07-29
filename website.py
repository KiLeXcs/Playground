from flask import Flask, request
app = Flask(__name__)

info = []

@app.route('/save', methods = ["POST"])
def save():
    data = {"info": request.json["info"]}
    info.append(data)
    return "Данные сохранены"

@app.route('/read/<int:number>', methods = ["GET"])
def read(number):
    return info[number-1]

@app.route('/readall', methods = ["GET"])
def readall():
    return info

if __name__ == '__main__':
   app.run(debug = True)