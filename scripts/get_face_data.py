import requests
import os, time, json

api_url = 'https://api.projectoxford.ai/face/v1.0/detect'

payload = {
			'returnFaceAttributes': 'age,gender,smile,glasses',
			'returnFaceLandmarks': 'true',
		   }

headers = {
			'Content-Type': 'application/json',
			'Ocp-Apim-Subscription-Key': 'your sub key',
		  }



for dir in os.listdir('images-with-data'):
	face_data_for_dir = []
	print 'images-with-data/' + dir
	for image in os.listdir('images-with-data/' + dir):
		url = 'http://public facing path to images/%s/%s' % (dir, image)

		request_data = {
    		'url': url,
		   }
		print "facing %s/%s" % (dir, image)
		r = requests.post(api_url, json=request_data, headers=headers, params=payload)
		face_data = json.loads(r.text)
		print face_data
		if face_data and isinstance(face_data, list):
			face_data = json.loads(r.text)[0]
			face_data['localName'] = image
			face_data_for_dir.append(face_data)
		else:
			print "ERROR  %s/%s" % (dir, image)
		time.sleep(4)

	with open('images-with-data/' + dir + '/data.json', 'a') as outfile:
	    json.dump(face_data_for_dir, outfile, sort_keys=True, indent=4, separators=(',', ': '))