import requests
from os import listdir, rename
from os.path import isfile, join

# for each image in unprocess/dir_name/*
# grab data from ms api, update data.json
# 


headers = {
	'Ocp-Apim-Subscription-Key': 'your sub key',
}

params = {
	'url': 'http://hlslwebtest.law.harvard.edu/dev/matt/cenbar/',
	'returnFaceLandmarks': 'true',
	'returnFaceAttributes': 'age, gender, headPose, smile, facialHair, glasses',
	
}

#r = requests.post(headers=headers, params=params)

for dir in listdir('data/unprocessed/'):
	for f in listdir('data/unprocessed/' + dir):
		rename('data/unprocessed/' + dir + '/' + f, 'data/processed/' + f)


#print r.text