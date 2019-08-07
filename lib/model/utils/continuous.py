import numpy as np
# from scipy.misc import imread, imresize
import cv2
import torch
import math

# Parameters are as follows:
#   N:The interval between the extracted frames for correction
#   pascal_initial: The initial location of all subjects detected in the first frame
#   cls_dets: The locations of all subjects detected in the current frame
#   pascal_class: The class labels of all subjects detected in the current frame
#   pascalreturn1: A tensor of [vx, vy] for all subjects
#   pascalreturn2: The class labels of all subjects
#   NOTE: All locations/class labels for pascalreturn1 and pascalreturn2 start at index 1!

# oldfunction should:
#   Develop appropriate kinematic equations to determine where predicted locations are.
#   Find the closest subject of identical type.
#   If the Euclidean distance between the ground truth and predicted location exceeds
#   twice the hypotenuse of the bounding box, subtract from the score a decrement of N.
#   If the Euclidean distance between the ground truth and predicted location is less
#   than half the hypotenuse of the bounding box, add to the score an increment of N.
#   Scores to be altered are at line 24 of /models/components/proposal.py.

##############THIS FUNCTION IS BEING EDITED AT THE MOMENT##############
def oldfunction(interval, pascal_initial, pascal_class, cls_dets, pascalreturn1, pascalreturn2, pascalreturn3):
    counter = 1
    cls_dets2 = cls_dets
    while counter < pascal_initial.size()[0]:
        predictx = pascal_initial[counter][0] + (pascal_initial[counter][0] * interval)
        predicty = pascal_initial[counter][1] + (pascal_initial[counter][1] * interval)
        if pascalreturn2[counter] == "bottle":
            predicty = predicty - (23.33 * pascalreturn3[counter] * interval * interval)
        pascal_classcopy = pascal_class
        cls_detscopy = cls_dets
        # while pascal_classcopy.size > 2:
        if 1 == 1:
            counterinner = (cls_detscopy.size())[0] - 1
            distancemin = 10000
            specialhypotenuse = 10000
            outerx1 = torch.tensor([[0, 0, 0, 0, 0]])
            while counterinner > 0:
                if pascal_classcopy[counterinner] == pascalreturn2[counter]:
                     xmid = (cls_detscopy[counterinner][2] + cls_detscopy[counterinner][0])/2
                     ymid = (cls_detscopy[counterinner][3] + cls_detscopy[counterinner][1])/2
                     deltax = cls_detscopy[counterinner][2] - cls_detscopy[counterinner][0]
                     deltay = cls_detscopy[counterinner][3] - cls_detscopy[counterinner][1]
                     innerx1 = cls_detscopy[counterinner]
                     hypotenuse = math.sqrt(math.pow(deltax, 2) + math.pow(deltay, 2))
                     valuevar = math.sqrt(math.pow(xmid - predictx, 2) + math.pow(ymid - predicty, 2))
                     if distancemin > valuevar:
                         distancemin = valuevar
                         specialhypotenuse = hypotenuse
                         outerx1 = innerx1
                counterinner = counterinner - 1
            # cls_detscopy = np.vstack(row for row in cls_detscopy if row not in qwerty)
            # pascal_classcopy = np.vstack(row for row in pascal_classcopy if row not in asdfgh)
            if distancemin > 2 * specialhypotenuse:
                counterly = 0
                while counterly < (cls_dets2.size())[0]:
                    if cls_dets2[counterly] == outerx1:
                       error = distancemin/1000
                       cls_dets2[counterly][4] = cls_dets2[counterly][4] - error
                print("Decrement")
            if distancemin < specialhypotenuse/2:
                counteras = 0
                while counteras < (cls_dets2.size())[0]:
                    if cls_dets2[counteras] == outerx1:
                       improvement = 1 - (2*distancemin)/specialhypotenuse
                       cls_dets2[counteras][4] = cls_dets2[counteras][4] + improvement
                       if cls_dets2[counteras][4] > 1:
                           cls_dets2[counteras][4] = 1
                print("Increment")
        counter = counter + 1
    return cls_dets2