import math, json, os, random

from PIL import Image, ImageDraw


colors = [(255,87,136),(212,54,63),(176,255,30),(78,68,232),(18,255,199)]
#colors = [(255,87,222),(0,54,63)]
resize_factor = 2

path_to_source_images = '../data/source-images/'
path_to_altered_images = '../data/results/with-colored-bars/altered-images/'

face_data_for_dir = []

with open('../data/results/data.json', 'r') as file:
	data = json.loads(file.read())

	for image in data:
		for face in image:
			if '.DS_Store' in face['localName']:
				break

			filename = "%s%s" % (path_to_source_images, face['localName'])

			im = Image.open(filename)
			width, height = im.size
			im = im.resize([width  * resize_factor, height  * resize_factor], Image.ANTIALIAS)
			width, height = im.size
			draw = ImageDraw.Draw(im)

			x = face['faceLandmarks']['pupilLeft']['x'] * resize_factor
			y = face['faceLandmarks']['pupilLeft']['y'] * resize_factor
			x2 = face['faceLandmarks']['pupilRight']['x'] * resize_factor
			y2 = face['faceLandmarks']['pupilRight']['y'] * resize_factor

			# find the length of the line
			# we use this length to pad out the line on each side of the pupil
			length_of_line = math.sqrt((x2-x)**2 - (y2-y)**2)
			line_padding = length_of_line * .55

			# get the slope
			m = (y2-y)/(x2-x)
			b=-1*(m*x-y)

			# extrapolate our line left
			x3 = x - line_padding
			y3 = m*x3 + b

			# and extrapolate our line to the right
			x4 = x2 + line_padding
			y4 = m*x4 + b

			# draw our line with our two new points
			color = random.choice(colors)

			draw.line((x3,y3,x4,y4), fill=color, width=int(line_padding))

			del draw

			# resize back down
			im = im.resize([width/resize_factor, height/resize_factor], Image.ANTIALIAS)

			# write to new file
			outfile = "%s%s" % (path_to_altered_images, face['localName'])
			im.save(outfile)
			del im

			print "drew on %s" % outfile
