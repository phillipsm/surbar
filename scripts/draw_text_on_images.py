import glob
import exifread
from dateutil import parser
from datetime import timedelta
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


# open up an image in dir, read the 
# creation date from the exif data
# draw the time in the lower right of the image

font = ImageFont.truetype("/Users/phillipsm/Library/Fonts/PostGrotesk-Light.otf", 100)

for image in glob.glob('../data/source-images/*'):

    #add nine hours and 45 mins to exif time
    f = open(image, 'rb')

    # get exif tags
    tags = exifread.process_file(f)

    if tags:
        exif_date = str(tags['EXIF DateTimeOriginal'])
        dt = parser.parse(exif_date)
        dt = dt + timedelta(hours=9, minutes=45)
        adjusted_time = dt.strftime('%I:%M:%S')

        im = Image.open(image)
        draw = ImageDraw.Draw(im)
        width, height = im.size
        draw.text((width - 450, height - 135), adjusted_time, (255,255,255), font=font)
        im.save(image)
        del draw, im
        print "added %s to %s" % (adjusted_time, image)
    else:
        print "couldn't process %s" % image