import numpy as np
# from scipy.misc import imread, imresize
import cv2

# oldfunction should:
#   1. From pascalreturn4, determine whether gravity and/or another resistive force should be
#      incorporated.
#   2. Iterate through pascalreturn3, using appropriate kinematic equations to determine where
#      pascal_class's coordinates are predicted to be located.
#   3. Iterate through pascal_class, finding the closest subject of identical type.
#   4. For each iteration, if the Euclidean distance between the two exceeds twice the
#      hypotenuse of the bounding box, add to a tensor a decrement of N.
#   5. For each iteration, if the Euclidean distance between the two is less than half
#      the hypotenuse of the bounding box, add to a tensor an increment of N.
#   6. Using the tensor, alter the scores at line 24 of /models/components/proposal.py.

def oldfunction(pascal_class, cls_dets, pascalreturn3, pascalreturn4):
    return pascal_class
