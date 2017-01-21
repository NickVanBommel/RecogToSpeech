import requests as r
import json as j
import SimpleCV as scv
import time as t
import os as o

key = '2fe59ee611974c92ba91b28b94dfd370' 

#get photo
cam = scv.Camera()
cam.getImage().save("img.jpg")

#url, headers, file location
url = "https://api.projectoxford.ai/vision/v1.0/analyze?visualFeatures=Description&language=en"
headers = {'Ocp-Apim-Subscription-Key': key}
files = {'file': open('img.jpg', 'rb')}

#sends photo to microsoft and gets info
response = r.post(url, headers=headers, files=files)

#parse response
data = j.loads(response.text)
caption = data['description']['captions'][0]['text']

print(caption)

#o.rename('img.jpg', data['requestId'] + '.jpg')
