#!C:\Program Files (x86)\Python36-32\python.exe
# -*- coding: utf-8 -*-
import sqlite3
import html
import json

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

class Requests:
    def __init__(self, request):
        self.request = request

    def getLabels(self):
        cursor.execute("SELECT * FROM labels")
        labels = cursor.fetchall()
        i = 0
        while i < len(labels):
            data = {"id": labels[i][0], "coordinates": labels[i][1], "description": labels[i][2], "type": labels[i][3]}
            if len(row) - 1 == i and i != 0:
                s += json.dumps(data)
            elif i == 0 and len(row) - 1 == 0:
                s = json.dumps(data)
            elif i == 0:
                s = json.dumps(data) + ','
            else:
                s += json.dumps(data) + ','

            i = i + 1
        print('{ "users": [' + s + "]}")

    def executeRequest(self, request):
        if request == "getLabels":
            getLabels()

