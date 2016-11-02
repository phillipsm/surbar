import math, json, os, random

from PIL import Image, ImageDraw


#colors = [(255,87,136),(212,54,63),(176,255,30),(78,68,232),(18,255,199)]
colors = [(255,87,222),(0,54,63)]
resize_factor = 8

face_data_for_dir = []

with open('data/data.json', 'r') as file:
	data = json.loads(file.read())

	for image in data:
		filename = "data/processed/%s" % image['localName']

		im = Image.open(filename)
		width, height = im.size
		im = im.resize([width  * resize_factor, height  * resize_factor], Image.ANTIALIAS)
		width, height = im.size
		draw = ImageDraw.Draw(im)


		x = image['faceLandmarks']['pupilLeft']['x'] * resize_factor
		y = image['faceLandmarks']['pupilLeft']['y'] * resize_factor
		x2 = image['faceLandmarks']['pupilRight']['x'] * resize_factor
		y2 = image['faceLandmarks']['pupilRight']['y'] * resize_factor

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
		lil_folks = ['antiphysical.png', 'baldy.png', 'basidiophore.png', 'bluegrass.png', 'enterostasis.png', 'flogmaster.png', 'freit.png', 'nicolaitan.png', 'superendow.png', 'tillotter.png', ]
		if image['localName'] in lil_folks:
			color = (176, 255, 48)
		else:
			color = random.choice(colors)

		draw.line((x3,y3,x4,y4), fill=color, width=int(line_padding))

		del draw

		# write to stdout
		outfile = "data/processed/%s" % image['localName']
		im = im.resize([width/resize_factor, height/resize_factor], Image.ANTIALIAS)
		im.save(outfile, "PNG")

		print "just finished %s" % outfile
