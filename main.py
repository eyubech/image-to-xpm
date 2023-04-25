import sys
from wand.image import Image


argc = len(sys.argv)
if (argc < 2):
    print("Please provide the path to the image file 'to_xpm' command.")
    print("For example: 'to_xpm ./image.png'")
    exit()
if (argc > 2):
    print("Too many arguments")
    exit()

img = sys.argv[1]
output = ""
for _ in img:
    if _ == '.': break
    output += _
output += '.xpm'

try:
    with Image(filename=img) as img:
        img.format = 'xpm'
        xpm_data = img.make_blob(format='xpm')
    with open(output, 'wb') as f:
        f.write(xpm_data)
except:
    print("Please check the image path or the config file is executed.")

