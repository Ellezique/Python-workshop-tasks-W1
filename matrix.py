#!/usr/bin/python3

#NOTE TO SELF: CV2 is installed with my Pyhton 3.6
import numpy as np
import skimage 
import skimage.draw
#import skimage.draw import line_aa
import cv2 
# np.zeros(matrix)
# height = matrix.shape[0]
# width = matrix.shape[1]

def draw_line_segment(shape, start_coordinate, end_coordinate):
  from skimage.draw import line
  img = (np.zeros((shape), dtype=np.uint8))
  rr, cc = line(start_coordinate[0], start_coordinate[1], end_coordinate[0], end_coordinate[1])
  img[rr, cc] = 255 
  return img

image = draw_line_segment([100, 100], [10, 10], [20, 20])
#print(draw_line_color([10, 10], [1, 1], [8, 8]))
#image = np.multiply(image, 128)
cv2.imwrite('image.jpg',image)

