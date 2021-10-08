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


def downloadImage():
    #fh = open("imageToSave.png", "wb")
    #fh.write(image.decode('base64'))
    ##fh = open("image.png", "w+")
    ##fh.write(image.decodebytes('base64'))
    #image_ = base64.decodestring(image)
    #fh.write(image)
    ##fh.close()
    with open("in.png", "rb") as original_file:
        encoded_string = base64.b64encode(original_file.read())
    encoded_string = codecs.encode("iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAABmJLR0QA/wD/AP+gvaeTAAAE3UlEQVR4nO2aW4hVVRiAv8ZpvJbirdMURV6x8hpdEDKwIAkl0jLyJZAYsgclCqcXwdKHogzUpyAoSAmiy8MQ+WJEFyVqvCA6dhGcJCN1vDWTziize/jPxjX7rLX32mutfcah/cH/cM7e67/xr73/tdaGkpKSkpKS65Em4D0gSsgXg+HMRqANmFIne83AHmqDvwjcnjLuHuDN0M5sVBz4t/p7RGgjCguBk9QGHwFrM8bGvgZLghq8KseAZaGMKLQAvQabPwHDMsYfVu4PkoQ2gzOxPBjCiEJcwl0JO1eABRZjk/55J2EKcEmjOJYdvgaqjAbGJ36vBvZW7bxjoUNXredCOGeaBhFSrpUANu4FzgMbgJsS12YjCclCLf9Y9gfwjZHInDcl4SOy52YWDyn6TgOvVO3aoiv/oK/MZQYDsXwM3Oih/zGNzr+BVmC4xXhTlb7r4VMN9yGNiemZ0Ib76/FJg84I6ETeDo0p43XlHwHrHP1JpYKUvc7gLmCUg85VBn2qdAArgRsSY03lHyGJLYQGYKfB6LfAzTn1tRh06eQQ8AzXEpH2kJ7rEpwtjchDRmf4Rwa+1rJ42aAnTfYAizGXfwSM84jPiibgS4Pxw0hPb8MGgw4fOWtjuMHSQRN9wNPAN5prdwNfk754ibF5z+fluM1NvgkAeSssBb7XXJtZ/X9aho4hnQCAHiQJ+zTX7gS+Q7o9E2MC+aFS1wQAXACWAEc01yrAbmCeYWwRFdBZgE4rbsPcOp8FHtCMMT1IfWRREcHZchdwQuNUhOzqqM49i0yhkMF3kN451oWZSD+vc7AHmS6bgH7DPa5ygoIboDzMoXZzI5ZQgfcDvwGfAGvI2fwk++oimI/0AyG6sqvAr0A70mgdQTrCrgC6C2URbvP8L2Absjs0H+k8hyzbyRd8D7IEH/IMQzYn887r5wbD2dCMBb4if+m/oeiYjf+W26AwlfSlqkk+51qHOgb4E9loGVtH3715GDhF/uD3M7AtVqfOIaTBuu5pQZbJeYM/zcAApwGXE/ecAR6pRxAuNAJbcWtm+qgNzLQ+uAw8X2wo+RmPrPZcu7kXEvqWWozZStjVrDMzgKO4B/92Ql8T8Ivl2M8oZiltzRLkSMs1+F3UvuJey6njAHBHQfGlsg7pzV2D76B2fVBBNlby6joJ3F9IlBqGAx84OKlKFzBdo3uHh85LyAFLoUxEdoB9gr8CPKrRvRD/JXI/0jsUssqdB/zh6WAEvGTQvxi3/kEnOwn8Gc8KoDuAY+9n2FkdwEYsewnz7QIrCLN7sxu7I/S3AtiK5Tgwyz10mIxsYvo68jswwdJmA/BpAJux6A5srNmcUNYLrEfO/JqRDxhMX3XFcgE5JsvDKOSANUQCevIGrXIwoaxVc09rivGrwBOOtitICYeoPmeSDz7daW9zivFXfYwjx2kujZEq23wc+Af3BHzoY1jhcaR3cAm+D1mrOHMgoVA3BXS9+w/Yfdxky4saGzayxdfwpoTCXiQJaQ/BTuAWX8MatpAv+HYCNEOTyDcHuzGfAPvSgPmTnKQcA24NZXg5do1QP9I0Fclo4OcMP9oJGHzMctIr4TzwVGijBprRr0n6kGlS2Kf8E5H9+n1IqXcj2X69eq2ezEI6vG7kYHQ7nk/7kpKSkpKS/yH/AUwJKpl7Bl0bAAAAAElFTkSuQmCC")
    #print(encoded_string)
    encoded_string = codecs.encode(image)
    # xmzWowsfJbpGwCe0DTveqwvos7Mf0lcVNe/Q+G1hO/p+UNPd/stUse8AhP/3fDixf8HI3No67nvhlYAAAAASUVORK5CYII='

    #print(type(encoded_string))
    # <class 'bytes'>

    """
    2nd step - create new image using the encoded string
    """
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


