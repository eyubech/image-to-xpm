from wand.image import Image

# Input image file path
input_image = "ayoub.png"  # Replace with the path to your input image file

# Read input image using MagickWand
with Image(filename=input_image) as img:
    # Convert image to XPM format
    img.format = 'xpm'
    xpm_data = img.make_blob(format='xpm')

# Write XPM data to output file
with open('output.xpm', 'wb') as f:
    f.write(xpm_data)
