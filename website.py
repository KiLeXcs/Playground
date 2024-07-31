from flask import Flask, request
app = Flask(__name__)

info = []

@app.errorhandler(404)
def page_not_found(e):
    return "Такой страницы не существует"

def check(number):
    if number > len(info) or number == 0:
        return False
    return True

@app.route('/', methods = ["GET"])
def main():
    return "Главная страница"

@app.route('/save', methods = ["POST"])
def save():
    data = {"info": request.json["info"]}
    info.append(data)
    return "Данные сохранены"

@app.route('/read/<int:number>', methods = ["GET"])
def read(number):
    if check(number):
        return info[number-1]
    else:
        return "Таких данных не существует"

@app.route('/delete/<int:number>', methods = ["GET"])
def delete(number):
    if check(number):
        info.remove(info[number-1])
        return f"Данные ячейки {number} удалены"
    else:
        return "Таких данных не существует"

@app.route('/readall', methods = ["GET"])
def readall():
    if len(info) > 0:
        return info
    return "Никаких данных не записано"

@app.route('/deleteall', methods = ["GET"])
def deleteall():
    global info
    if len(info) != 0:
        info = []
        return "Все данные удалены"
    return "Никакие данные не были записаны"

if __name__ == '__main__':
   app.run(debug = True)