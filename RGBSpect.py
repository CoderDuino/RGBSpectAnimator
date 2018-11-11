from PIL import Image
import numpy as np
import time
start_time = time.time()

#Settings
Vibrance = 40
Frame = 1000
FramesPerSecond = 10
ResX = 1366
ResY = 768

print("calculating..")

ColorShift = -100
imgs = [None] * Frame
# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
for l in range(0,Frame):
    img = Image.new( 'RGB', (ResX,ResY), "black") # create a new black image
    pixels = img.load() # create the pixel map

    for i in range(img.size[0]):    # for every col:
        for j in range(img.size[1]):    # For every row
            pixels[i,j] = (i+ColorShift, j+ColorShift, Vibrance) # set the colour accordingly
    imgs[l] = img
    ColorShift+=1
    if l % 20 == 1:
        print("frames calculated: "+str(l))

bkimgs = [None] * Frame
# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
for l in range(0,Frame):
    img = Image.new( 'RGB', (ResX,ResY), "black") # create a new black image
    pixels = img.load() # create the pixel map

    for i in range(img.size[0]):    # for every col:
        for j in range(img.size[1]):    # For every row
            pixels[i,j] = (i+ColorShift, j+ColorShift, Vibrance) # set the colour accordingly
    bkimgs[l] = img
    ColorShift-=1
    if l % 20 == 1:
        print("frames calculated: "+str(l))
imgout = [None]*Frame*2

cntr = 0
for n in imgs:
    imgout[cntr] = n
    cntr+=1
for n in bkimgs:
    imgout[cntr] = n
    cntr+=1

print("finished calculating "+str(Frame)+" frames!")
print("assembling...")
imgout[0].save('RGBSpect_Animate.gif',
               save_all=True,
               append_images=imgout[1:],
               duration=Frame/FramesPerSecond,
               loop=0)
print("assembled!")
print("Finished in ", time.time() - start_time, "s")
