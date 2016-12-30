import math, json, os, random, glob

from PIL import Image, ImageDraw

# draw censor bars on images, but make them sticky
# that is, they stick, or add, to the subsequent
# frames

colors = [(255,87,136),(212,54,63),(176,255,30),(78,68,232),(18,255,199)]
#colors = [(255,87,222),(0,54,63)]
resize_factor = 2

path_to_source_images = '../data/source-images/'
path_to_altered_images = '../data/results/with-colored-bars-additive/altered-images/'

face_data_for_dir = []
sticky_bars = []


# get our existing data on our images
with open('../data/results/data.json', 'r') as file:
		data = json.loads(file.read())

import pdb
#pdb.set_trace()
# loop through every image and draw, additively, censor bars
for image in glob.glob(path_to_source_images + '*'):
	for image_entry_set in data:
		for image_entry in image_entry_set:
			if image_entry['localName'] == os.path.basename(image):
				# save our bar for subsequent images
				sticky_bar = {'x1': image_entry['faceLandmarks']['pupilLeft']['x'],
							  'y1': image_entry['faceLandmarks']['pupilLeft']['y'],
							  'x2': image_entry['faceLandmarks']['pupilRight']['x'],
							  'y2': image_entry['faceLandmarks']['pupilRight']['y'],
							  'color': random.choice(colors) }
				sticky_bars.append(sticky_bar)

	print "number of stickies, %s" % len(sticky_bars)

	# draw all of our sticky bars
	filename = image
	im = Image.open(filename)
	width, height = im.size
	im = im.resize([width  * resize_factor, height  * resize_factor], Image.ANTIALIAS)
	width, height = im.size
	draw = ImageDraw.Draw(im)

	for sticky in sticky_bars:
		x = sticky['x1'] * resize_factor
		y = sticky['y1'] * resize_factor
		x2 = sticky['x2'] * resize_factor
		y2 = sticky['y2'] * resize_factor

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
		draw.line((x3,y3,x4,y4), fill=sticky['color'], width=int(line_padding))

	del draw

	# resize back down
	im = im.resize([width/resize_factor, height/resize_factor], Image.ANTIALIAS)

	# write to new file
	outfile = "%s%s" % (path_to_altered_images, os.path.basename(image))
	im.save(outfile)
	del im
	print "drew on %s" % outfile