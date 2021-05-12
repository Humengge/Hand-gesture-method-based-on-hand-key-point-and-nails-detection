import pandas as pd
import json
import os
import csv

def chooseRightHand(data):
    temp = 0
    hand = {}
    for i in data:
        location = i.get('location')
        area = int(location.get('height')) * int(location.get('width'))
        temp = max(temp, area)
        if temp == area: 
            hand = i
    return hand

def writeToCsv(info, name, savePath):
    keyPoints = info.get('hand_parts')
    data_raw = []
    for i in range(21):
        coordinates = keyPoints.get(str(i))
        data_raw.append(int(coordinates.get('x')))
        data_raw.append(int(coordinates.get('y')))
    data_raw.append(int(name[-6]))
    # if name[-7] == 'b':
    #     data_raw.append(1)
    # elif name[-7] == 's':
    #     data_raw.append(0)
    # elif name[-7] == 'g':
    #     data_raw.append(2)
    data_raw.append(name[-7])
    with open(savePath, 'a', newline='') as c:
        csv_writer = csv.writer(c)
        csv_writer.writerow(data_raw)

path = "keyPointsInfo/informations/"
savePath = "finalData.csv"
fileNames = os.listdir(path)
for name in fileNames:
    f = open(path+name,"r",encoding="utf-8") 
    data = json.load(f)
    if len(data) == 1:
        writeToCsv(data[0], name, savePath)

    elif len(data) > 1:
        hand = chooseRightHand(data)
        writeToCsv(hand, name, savePath)


        