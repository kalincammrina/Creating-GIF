import imageio.v3 as iio

image_folder = './images'

filenames = ['GIF/chicklet1.png', 'GIF/chicklet2.png', 'GIF/chicklet3.png', 'GIF/chicklet4.png']
images =  './images'

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('GIF/Chick.gif', images, duration = 500, loop = 0)






