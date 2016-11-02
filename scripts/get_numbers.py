import json, os


for dir in os.listdir('images-with-data'):

	dept_nums = {'female': 0, 'male': 0, 'avg_age': 0, 'ages':[], 'glasses': 0, 'avg_smile': 0}

	with open('images-with-data/' + dir + '/data.json') as data_file:
		faces = json.load(data_file)

	for face in faces:
		if face['faceAttributes']['gender'] == 'female':
			dept_nums['female'] += 1
		if face['faceAttributes']['gender'] == 'male':
			dept_nums['male'] += 1

		if face['faceAttributes']['glasses'] == 'NoGlasses':
			dept_nums['glasses'] += 1

		dept_nums['avg_smile'] += face['faceAttributes']['smile']

		dept_nums['avg_age'] += face['faceAttributes']['age']
		dept_nums['ages'].append(face['faceAttributes']['age'])


	dept_nums['avg_age'] = dept_nums['avg_age']/len(faces)
	dept_nums['avg_smile'] = dept_nums['avg_smile']/len(faces)
	dept_nums['ages'].sort()

	print dir
	print "%s people" % len(faces)
	print "average age, %s" % dept_nums['avg_age']
	print "ages, " + str(dept_nums['ages'])
	print "average smile, %s" % dept_nums['avg_smile']
	print "%s female, %s male" % (dept_nums['female'], dept_nums['male'])
	print '============================'
