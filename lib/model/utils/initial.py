import numpy as np
# from scipy.misc import imread, imresize
import cv2

# newfunction should:
#   1. See the whiteboard in lab.
#   2. Find the two subjects of minimal distance and calculate velocity and acceleration.
#      Remove them from the tensors/arrays. Add the velocity and acceleration to four tensors
#      (vx, vy, ax, ay). Add the pascal_class into an array.
#   3. Repeat step 2 until completed.
#   4. Return the tensors and the array.

def newfunction(f, x, i, a, k, y):
    flipped = 0
    oddnum = 0
    lst = list(f)
    lst2 = list(i)
    lst3 = list(f)
    lst4 = list(i)
    f2 = 0
    i2 = 0
    while lst[f2] != lst2[i2]:
       while lst[f2] < lst2[i2]:
          f2 = f2 + 1
       while lst[f2] > lst2[i2]:
          i2 = i2 + 1
    f3 = f2
    i3 = i2
    fcount = 0
    icount = 0
    while lst[f3] == lst[f3 + 1]:
       fcount = fcount + 1
       f3 = f3 + 1
    while lst2[i3] == lst2[i3 + 1]:
       icount = icount + 1
       i3 = i3 + 1
    if fcount > icount:
       flipped = 1
       lst3 = lst(i)
       lst4 = lst(f)
       igoogol = f2
       f2 = i2
       i2 = igoogol
       if icount % 2 == 1:
          oddnum = 1
    else:
       if fcount % 2 == 1:
          oddnum = 1
    # At this point, lst3[f2] and lst4[i2] will store the starting location at which to compare
    # locations.
    return f, x, i, a
