import numpy as np
# from scipy.misc import imread, imresize
import cv2

# Parameters are as follows:
#   pascal_class: The locations of all subjects detected in the current frame
#   cls_dets: The class labels of all subjects detected in the current frame
#   pascalreturn1: A tensor of [vx, vy] for all subjects
#   pascalreturn2: The class labels of all subjects predicted
#   NOTE: All locations/class labels for pascalreturn1 and pascalreturn2 start at index 1!

# oldfunction should:
#   Develop appropriate kinematic equations to determine where predicted locations are.
#   Find the closest subject of identical type.
#   If the Euclidean distance between the ground truth and predicted location exceeds
#   twice the hypotenuse of the bounding box, subtract from the score a decrement of N.
#   If the Euclidean distance between the ground truth and predicted location is less
#   than half the hypotenuse of the bounding box, add to the score an increment of N.
#   Scores to be altered are at line 24 of /models/components/proposal.py.

def oldfunction(pascal_class, cls_dets, pascalreturn1, pascalreturn2):
    np.asarray([0])
