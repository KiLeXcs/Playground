import requests

count = 0

if requests.get("http://127.0.0.1:5000/").json()["Status"] == "OK":
    print ("Просто обращаемся на главную страницу --- Success")
    count += 1
else:
    print ("Просто обращаемся на главную страницу --- Failed")

if requests.get("http://127.0.0.1:5000/read/1").json()["Status"] == "ERROR":
    print ("Пытаемся прочитать данные, которые еще не записаны --- Success")
    count += 1
else:
    print ("Пытаемся прочитать данные, которые еще не записаны --- Failed")

if requests.get("http://127.0.0.1:5000/readall").json()["Status"] == "ERROR":
    print ("Пытаемся прочитать сразу все данные --- Success")
    count += 1
else:
    print ("Пытаемся прочитать сразу все данные --- Failed")

if requests.get("http://127.0.0.1:5000/delete/1").json()["Status"] == "ERROR":
    print ("Пытаемся удалить данные, которые еще не записаны --- Success" )
    count += 1
else:
    print ("Пытаемся удалить данные, которые еще не записаны --- Failed" )

if requests.get("http://127.0.0.1:5000/deleteall").json()["Status"] == "ERROR":
    print ("Пытаемся удалить сразу все данные --- Success")
    count += 1
else:
    print ("Пытаемся удалить сразу все данные --- Failed")

for i in range (5):
    data = {"Info": i}
    if requests.post("http://127.0.0.1:5000/save", json = data).json()["Status"] == "OK":
        print (f"Сохраняем {i} --- Success")
        count += 1
    else:
        print (f"Сохраняем {i} --- Failed")

if requests.get("http://127.0.0.1:5000/read/1").json()["Status"] == "OK":
    print ("Пытаемся прочитать данные 1 ячейки --- Success")
    count += 1
else:
    print ("Пытаемся прочитать данные 1 ячейки --- Failed")

if requests.get("http://127.0.0.1:5000/read/6").json()["Status"] == "ERROR":
    print ("Пытаемся прочитать данные 6 ячейки --- Success")
    count += 1
else:
    print ("Пытаемся прочитать данные 6 ячейки --- Failed")

if requests.get("http://127.0.0.1:5000/readall").json()["Status"] == "OK":
    print ("Пытаемся прочитать сразу все данные --- Success")
    count += 1
else:
    print ("Пытаемся прочитать сразу все данные --- Failed")

if requests.get("http://127.0.0.1:5000/delete/1").json()["Status"] == "OK":
    print ("Пытаемся удалить данные 1 ячейки --- Success")
    count += 1
else:
    print ("Пытаемся удалить данные 1 ячейки --- Failed")

if requests.get("http://127.0.0.1:5000/readall").json()["Status"] == "OK":
    print ("Пытаемся прочитать сразу все данные после удаления --- Success")
    count += 1
else:
    print ("Пытаемся прочитать сразу все данные после удаления --- Failed")

if requests.get("http://127.0.0.1:5000/deleteall").json()["Status"] == "OK":
    print ("Пытаемся удалить сразу все данные --- Success")
    count += 1
else:
    print ("Пытаемся удалить сразу все данные --- Success")

if requests.get("http://127.0.0.1:5000/readall").json()["Status"] == "ERROR":
    print ("Пытаемся прочитать сразу все данные --- Success")
    count += 1
else:
    print ("Пытаемся прочитать сразу все данные --- Success")

print ("\n" + "-"*100 + "\n" + f"{count}/17 tests passed\n" + "-"*100)