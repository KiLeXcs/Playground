# Playground

**Hello world!**

To test this programs you need go to *127.0.0.1:5000* on your **browser**

## API

**API** | **url**
:-:|:-:|
main page | *127.0.0.1:5000/*
save info | *127.0.0.1:5000/save*
read all info | *127.0.0.1:5000/readall*
read information by cell number | *127.0.0.1:5000/read/number*
delete all info | *127.0.0.1:5000/deleteall*
delete information by cell number | *127.0.0.1:5000/delete/number*
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
 
To run programs you need to do next steps:
- open cmd
- git clone https://github.com/KiLeXcs/Playground
- cd Playground
- python3 website.py

It's all left
