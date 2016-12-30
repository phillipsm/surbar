import math, json, os, random

from PIL import Image, ImageDraw


colors = [(255,87,136),(212,54,63),(176,255,30),(78,68,232),(18,255,199)]
#colors = [(255,87,222),(0,54,63)]
resize_factor = 10

face_data_for_dir = []
width, height = (2592, 1944)
import pdb
#pdb.set_trace()

infile = '/Users/phillipsm/Desktop/100GOPRO/G0020660.JPG'
outfile = "data/with-bars/combined-bg.png"
with open('data/data.json', 'r') as file:
	data = json.loads(file.read())


	if os.path.exists(infile):
		im = Image.open(infile)
	else:
		im = Image.new('RGBA', (width, height), (255,255,255,0))

	im = im.resize([width  * resize_factor, height  * resize_factor], Image.ANTIALIAS)
	width, height = im.size
	


	for image in data:
		for face in image:
			if '.DS_Store' in face['localName']:
				break

			print "Processing %s" % face['localName']


			


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
			draw = ImageDraw.Draw(im)
			draw.line((x3,y3,x4,y4), fill=color, width=int(line_padding))
			del draw

			
	# write to stdout
	im = im.resize([width/resize_factor, height/resize_factor], Image.ANTIALIAS)
	im.save(outfile, "PNG")
	print "just finished %s" % outfile
