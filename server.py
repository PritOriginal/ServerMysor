#!C:\Program Files (x86)\Python36-32\python.exe
# -*- coding: utf-8 -*-
import base64
import cgi
import codecs
import sqlite3
import html
import json
import sys


def getLabels():
    cursor.execute("SELECT * FROM labels")
    labels = cursor.fetchall()
    i = 0
    while i < len(labels):
        data = {"id": labels[i][0], "coordinates": labels[i][1], "description": labels[i][2], "type": labels[i][3]}
        if len(labels) - 1 == i and i != 0:
             s += json.dumps(data)
        elif i == 0 and len(labels) - 1 == 0:
             s = json.dumps(data)
        elif i == 0:
            s = json.dumps(data) + ','
        else:
            s += json.dumps(data) + ','

        i = i + 1
    print('{ "labels": [' + s + "]}")


def addLabels():
    cursor.execute("INSERT INTO labels (coordinates, description, type) VALUES (?,?,?)", (coordinates, description, type))
    conn.commit()
    encoded_string = codecs.encode(image)
    with open("new_image.png", "wb") as new_file:
        new_file.write(base64.decodebytes(encoded_string))
    data = {"request": "ok"}
    s = json.dumps(data)
    print(s)


def downloadImage():
    encoded_string = codecs.encode(image)
    with open("new_image.png", "wb") as new_file:
        new_file.write(base64.decodebytes(encoded_string))
    data = {"request": "ok"}
    s = json.dumps(data)
    print(s)


def executeRequest(request):
    if request == "getLabels":
        getLabels()
    if request == "addLabels":
        if coordinates != "" and description != "" and type != "":
            addLabels()
    if request == "downloadImage":
        downloadImage()


sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()

request = form.getfirst("REQUEST","")
coordinates = form.getfirst("COORDINATES","")
description = form.getfirst("DESCRIPTION","")
type = form.getfirst("TYPE","")
image = form.getfirst("IMAGE","")
request = html.escape(request)
coordinates = html.escape(coordinates)
description = html.escape(description)
type = html.escape(type)
image = html.escape(image)

print("Content-Type: application/json\n")

conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

executeRequest(request)


