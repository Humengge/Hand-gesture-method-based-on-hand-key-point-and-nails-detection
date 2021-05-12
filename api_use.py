# encoding:utf-8
# -*- coding: utf-8 -*-
#!/usr/bin/env python

import urllib.parse
import urllib.request
import base64
import json
import time

import os

def draw_hands_point(path, savePath, originfilename,hands,resultfilename,pointsize,pointcolor):
    from PIL import Image, ImageDraw
 
    image_origin = Image.open(path+originfilename)
    draw =ImageDraw.Draw(image_origin)
    
    for hand in hands:
        
        for hand_part in hand['hand_parts'].values():
            #print(hand_part)
            draw.ellipse((hand_part['x']-pointsize,hand_part['y']-pointsize,hand_part['x']+pointsize,hand_part['y']+pointsize),fill = pointcolor)
        gesture = hand['location'] 
        draw.rectangle((gesture['left'],gesture['top'],gesture['left']+gesture['width'],gesture['top']+gesture['height']),outline = "red")
    
    
    image_origin.save(savePath+"/images/"+resultfilename, "JPEG")
 


def hand_analysis(path, savePath, filename,resultfilename,pointsize,pointcolor):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/hand_analysis"
    print(filename)
    
    f = open(path+filename, 'rb')
    img = base64.b64encode(f.read())
    
    params = dict()
    params['image'] = img
    params = urllib.parse.urlencode(params).encode("utf-8")
    #params = json.dumps(params).encode('utf-8')
    
    # access_token = get_token()
    begin = time.perf_counter()
    request_url = request_url + "?access_token=" + '24.93a77997cff7bf42c8ef760bd5d9d32c.2592000.1620200643.282335-23933490'
    request = urllib.request.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib.request.urlopen(request)
    content = response.read()
    end = time.perf_counter()
 
    print('Time:'+'%.2f'%(end-begin)+'s')
    if content:
        #print(content)
        content=content.decode('utf-8')
        #print(content)
        data = json.loads(content)
        # print('hand_num:',data['hand_num'])
        # print('hand_info:',data['hand_info'])
        # print('hand_info:',data['hand_info'])
        #print(data)
        result=data['hand_info']

        file = list(filename.split('.'))
        file.remove(file[1])
        txtName = ''.join(file)
        with open(savePath+"/informations/"+txtName+".txt", "w") as fp:
            fp.write(json.dumps(result, indent=4))
        f.close()
        
        draw_hands_point(path, savePath, filename,result,resultfilename,pointsize,pointcolor)

if __name__ =='__main__':
    path = "./dataAndLabel/"
    compare = "./keyPointsInfo/images/"
    files = os.listdir(path)
    compare = os.listdir(compare)
    nameSet = set(files).difference(set(compare))
    savePath = "./keyPointsInfo/"
    
    for filename in nameSet:
        hand_analysis(path, savePath, filename, filename, 20,'#800080')
