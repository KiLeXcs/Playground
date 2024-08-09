# Playground

**Hello world!**

To test this programs you need go to *127.0.0.1:5000* on your **browser**

## API

**API** | **HTTP request** |**url**
:-:|:-:|:-:|
main page | ***get*** |  *127.0.0.1:5000/*
save info | ***post*** |*127.0.0.1:5000/save*
read all info | ***get*** |*127.0.0.1:5000/readall*
read information by cell ***number*** | ***get*** | *127.0.0.1:5000/read/**number***
delete all info | ***get*** |*127.0.0.1:5000/deleteall*
delete information by cell ***number*** | ***get*** |*127.0.0.1:5000/delete/**number***
---

## How to save info

You need do *Post request* and send *json* in the following form:
```
{
    "Info": "You're information"
}
```
## Status

**Code status** | **Description**
:-:|:-:|
OK|Everything work good|
ERROR|Some issues|
---

## Run programs
 
To run this website you need to do next steps:
1. Open cmd
2. Print next commands:
    - git clone https://github.com/KiLeXcs/Playground
    - cd Playground
    - python3 website.py

## Test
Also you can test website with test.py.
This program doing all possible requests. If everyting work good, it will be print "Success", otherwise "Failed".

It's all right
