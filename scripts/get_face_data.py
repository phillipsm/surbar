import requests
import os, time, json

api_url = 'https://api.projectoxford.ai/face/v1.0/detect'

payload = { 'returnFaceId': 'true',
			'returnFaceAttributes': 'age,gender,smile,glasses',
			'returnFaceLandmarks': 'true',
		   }

headers = {
			'Content-Type': 'application/json',
			'Ocp-Apim-Subscription-Key': '',
		  }



import pdb, glob

#pdb.set_trace()
for image in glob.glob('data/processed/*'):#os.listdir('data/processed/'):
	

	url = 'http://location.tld/%s' % image
	request_data = {
		'url': url,
	   }
	print url
	r = requests.post(api_url, json=request_data, headers=headers, params=payload)
	face_data = json.loads(r.text)


	if face_data and isinstance(face_data, list):
		ff = []

		for face in face_data:
			face['localName'] = image
			ff.append(face)

		with open('data/data.json', 'r+') as f:
			stored_data = f.read()

			if stored_data:
				existing = json.loads(stored_data)
			else:
				existing = []

			existing.append(ff)

			f.seek(0)
			f.write(json.dumps(existing, sort_keys=True, indent=4, separators=(',', ': ')))
			f.truncate()

		print "%s has %s faces" % (image, len(face_data))

	else:
		print "ERROR %s" % image


	time.sleep(4)
