import numpy as np
# from scipy.misc import imread, imresize
import cv2

# newfunction2 should:
#   1. Store the values of newfunction into tensors by pascal_class
#   2. Store the values of newfunction2 into tensors by pascal_class
#   3. Compare the cls_dets(x1, y1, x2, y2) between tensors of the same pascal_class
#      but different function origin.
#   4. Find the two subjects of minimal distance and calculate velocity. Remove them
#      from the tensors. Add the velocity to a tensor (magnitude and direction). Add
#      the pascal_class into another tensor.
#   5. Repeat step 4 until completed.
#   6. Return two tensors, one for velocities, the other for pascal_class.

def newfunction(pascal_class, cls_dets):
    return pascal_class, cls_dets

def newfunction2(pascal_class, cls_dets, pascalreturn1, pascalreturn2):
    return pascal_class, cls_dets
