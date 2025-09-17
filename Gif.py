# Import required libraries
# - imageio.v3 (aliased as iio) for reading and writing images
# - os for working with file paths and directories

import imageio.v3 as iio

# A list to hold the loaded images
filenames = ['GIF/chicklet1.png', 'GIF/chicklet2.png', 'GIF/chicklet3.png', 'GIF/chicklet4.png']
images = [ ]

# Loop through each filename, load the image, and add it to the list
for filename in filenames:
  images.append(iio.imread(filename))

# Save the images as GIF
# - duration = 600 → each frame is displayed for 600 ms
# - loop=0 → the GIF repeats forever

iio.imwrite('GIF/Chick.gif', images, duration = 600, loop = 0)






