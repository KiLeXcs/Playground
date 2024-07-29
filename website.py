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

@app.route('/delete/<int:number>', methods = ["GET"])
def delete(number):
    info.remove(info[number-1])
    return "Данные удалены"

@app.route('/readall', methods = ["GET"])
def readall():
    return info

@app.route('/deleteall', methods = ["GET"])
def deleteall():
    global info
    info = []
    return "Все данные удалены"

if __name__ == '__main__':
   app.run(debug = True)