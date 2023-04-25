import sys
from wand.image import Image


argc = len(sys.argv)
if (argc < 2):
    print("Enter the image path after the command to_xpm example to_xpm ./image.png")
    exit

if (argc > 2):
    print("Too may arguments")
    exit


img = sys.argv[1]

output = ""

for _ in img:
    if _ == '.': break
    output += _
output += '.xpm'


with Image(filename=img) as img:
    img.format = 'xpm'
    xpm_data = img.make_blob(format='xpm')

with open(output, 'wb') as f:
    f.write(xpm_data)
