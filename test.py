import requests

print ("Просто обращаемся на главную страницу---" + requests.get("http://127.0.0.1:5000/").text)
print ("Пытаемся прочитать данные, которые еще не записаны---" + requests.get("http://127.0.0.1:5000/read/1").text)
print ("Пытаемся прочитать сразу все данные---" + requests.get("http://127.0.0.1:5000/readall").text)
print ("Пытаемся удалить данные, которые еще не записаны---" +requests.get("http://127.0.0.1:5000/delete/1").text)
print ("Пытаемся удалить сразу все данные---" + requests.get("http://127.0.0.1:5000/deleteall").text)

for i in range (10):
    data = {"info": i}
    print (f"Сохраняем {i}---" + requests.post("http://127.0.0.1:5000/save", json = data).text)

print ("Пытаемся прочитать данные 1 ячейки---" + requests.get("http://127.0.0.1:5000/read/1").text)
print ("Пытаемся прочитать данные 6 ячейки)---" + requests.get("http://127.0.0.1:5000/read/6").text)
print ("Пытаемся прочитать сразу все данные---" + requests.get("http://127.0.0.1:5000/readall").text)
print ("Пытаемся удалить данные 1 ячейки---" +requests.get("http://127.0.0.1:5000/delete/1").text)
print ("Пытаемся прочитать сразу все данные после удаления---" + requests.get("http://127.0.0.1:5000/readall").text)
##print ("Пытаемся удалить сразу все данные---" + requests.get("http://127.0.0.1:5000/deleteall").text)
print ("Все удалилось---" + requests.get("http://127.0.0.1:5000/readall").text)