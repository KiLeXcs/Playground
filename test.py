import requests

print ("Просто обращаемся на главную страницу---" + requests.get("http://127.0.0.1:5000/").json()["Status"])
print ("Пытаемся прочитать данные, которые еще не записаны---" + requests.get("http://127.0.0.1:5000/read/1").json()["Status"])
print ("Пытаемся прочитать сразу все данные---" + requests.get("http://127.0.0.1:5000/readall").json()["Status"])
print ("Пытаемся удалить данные, которые еще не записаны---" + requests.get("http://127.0.0.1:5000/delete/1").json()["Status"])
print ("Пытаемся удалить сразу все данные---" + requests.get("http://127.0.0.1:5000/deleteall").json()["Status"])

for i in range (5):
    data = {"Info": i}
    print (f"Сохраняем {i}---" + requests.post("http://127.0.0.1:5000/save", json = data).json()["Status"])

print ("Пытаемся прочитать данные 1 ячейки---" + requests.get("http://127.0.0.1:5000/read/1").json()["Status"])
print ("Пытаемся прочитать данные 6 ячейки---" + requests.get("http://127.0.0.1:5000/read/6").json()["Status"])
print ("Пытаемся прочитать сразу все данные---" + requests.get("http://127.0.0.1:5000/readall").json()["Status"])
print ("Пытаемся удалить данные 1 ячейки---" +requests.get("http://127.0.0.1:5000/delete/1").json()["Status"])
print ("Пытаемся прочитать сразу все данные после удаления---" + requests.get("http://127.0.0.1:5000/readall").json()["Status"])
print ("Пытаемся удалить сразу все данные---" + requests.get("http://127.0.0.1:5000/deleteall").json()["Status"])
print ("Пытаемся прочитать сразу все данные---" + (requests.get("http://127.0.0.1:5000/readall").json()["Status"]))