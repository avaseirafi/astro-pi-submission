# Import the libraries
from sense_hat import SenseHat
from time import sleep
from itertools import cycle, islice

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image
# Colour palette
a = (255, 255, 255) # White
b = (105, 105, 105) # DimGray
c = (0, 0, 0) # Black
d = (100, 149, 237) # CornflowerBlue
e = (0, 0, 205) # MediumBlue
f = (25, 25, 112) # MidnightBlue
g = (0, 191, 255) # DeepSkyBlue
h = (0, 255, 255) # Cyan
j = (143, 188, 143) # DarkSeaGreen
k = (46, 139, 87) # SeaGreen
l = (0, 255, 127) # SpringGreen
m = (34, 139, 34) # ForestGreen
n = (154, 205, 50) # YellowGreen
o = (128, 128, 0) # Olive
p = (240, 230, 140) # Khaki
q = (255, 255, 0) # Yellow
r = (184, 134, 11) # DarkGoldenrod
s = (139, 69, 19) # SaddleBrown
t = (255, 140, 0) # DarkOrange
u = (178, 34, 34) # Firebrick
v = (255, 0, 0) # Red
w = (255, 192, 203) # Pink
y = (255, 20, 147) # DeepPink
z = (153, 50, 204) # DarkOrchid


image = [
  [h, v, v, h, h, v, v, h, h, h, h, h, h, h, h, h],
  [v, v, v, v, v, v, v, v, h, h, h, h, h, h, h, h],
  [v, v, v, v, v, v, v, v, h, h, h, h, h, h, h, h],
  [h, v, v, v, v, v, v, h, h, h, h, h, h, h, h, h],
  [h, h, v, v, v, v, h, h, h, h, h, h, h, h, h, h],
  [m, h, h, v, v, h, h, m, h, h, h, h, h, h, h, h],
  [h, m, m, m, m, m, m, h, h, h, h, h, h, h, h, h],
  [h, h, h, m, m, h, h, h, h, h, h, h, h, h, h, h],
]
# A 8x8 multidimensional list pixel art map of circle
mask_pixels = [
 [a, a, a, a, a, a, a, a],
 [a, a, a, a, a, a, a, a],
 [a, a, a, a, a, a, a, a],
 [a, a, a, a, a, a, a, a],
 [a, a, a, a, a, a, a, a],
 [a, a, a, a, a, a, a, a],
 [a, a, a, a, a, a, a, a],
 [a, a, a, a, a, a, a, a],
]

for i in range(64):
    view = ([list(islice(cycle(row), i, i+8)) for row in image])
    # test if there is a white pixel in world_pixels if so
    # keep the pixel from view otherwise replace view's pixel
    # with the black from world_pixels
    view = [
        [
            view_pixel if mask_pixel == 'a' else mask_pixel
            for view_pixel, mask_pixel in zip(view_row, mask_row)
        ]
        for view_row, mask_row in zip(view, mask_pixels)
    ]

    # Initialize an empty list to hold the concatenated items
    concatenated_view_items = []
    
    # Iterate over each row in the 'view' matrix (assuming 'view' is a list of lists)
    for row in view:
        # Iterate over each item in the current row
        for item in row:
            # Append the current item to the list of concatenated items
            concatenated_view_items.append(item)

  
    sense.set_pixels(concatenated_view_items)
    sleep(0.6)

