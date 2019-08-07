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
def oldfunction(interval, pascal_initial, pascal_class, cls_dets, pascalreturn1, pascalreturn2, pascalreturn3, accels):
    counter = 1
    cls_dets2 = cls_dets
    if pascal_initial.size()[0] > 2:
      while counter < pascal_initial.size()[0]:
        predictx = pascal_initial[counter][0] + (pascalreturn1[counter][0] * interval)
        predicty = pascal_initial[counter][1] + (pascalreturn1[counter][1] * interval)
        print(pascalreturn2)
        print("Without g:", predictx)
        if pascalreturn2[counter] == "bottle":
            predictx = predictx + (0.5 * accels[counter][0] * interval * interval)
        print(predictx)
        print("Without g:", predicty)
        if pascalreturn2[counter] == "bottle":
            predicty = predicty + (0.5 * accels[counter][1] * interval * interval)
        print(predicty)
        pascal_classcopy = pascal_class
        cls_detscopy = cls_dets
        # while pascal_classcopy.size > 2:
        if 1 == 1:
            counterinner = 0
            distancemin = 10000
            specialhypotenuse = 10000
            outerx1 = torch.tensor([[0, 0, 0, 0, 0]])
            print((cls_detscopy.size())[0])
            while counterinner < pascal_classcopy.size:
                if pascal_classcopy == pascalreturn2[counter]:
                     xmid = (cls_detscopy[counterinner][2] + cls_detscopy[counterinner][0])/2
                     ymid = (cls_detscopy[counterinner][3] + cls_detscopy[counterinner][1])/2
                     deltax = cls_detscopy[counterinner][2] - cls_detscopy[counterinner][0]
                     deltay = cls_detscopy[counterinner][3] - cls_detscopy[counterinner][1]
                     innerx1 = cls_detscopy[counterinner]
                     hypotenuse = math.sqrt(math.pow(deltax, 2) + math.pow(deltay, 2))
                     valuevar = math.sqrt(math.pow(xmid - predictx, 2) + math.pow(ymid - predicty, 2))
                     print(valuevar)
                     if distancemin > valuevar:
                         distancemin = valuevar
                         specialhypotenuse = hypotenuse
                         outerx1 = innerx1
                counterinner = counterinner + 1
            # cls_detscopy = np.vstack(row for row in cls_detscopy if row not in qwerty)
            # pascal_classcopy = np.vstack(row for row in pascal_classcopy if row not in asdfgh)
            print("DistanceMin:", distancemin)
            print("Hypotenuse:", specialhypotenuse)
            if distancemin > 2 * specialhypotenuse:
                counterly = 0
                while counterly < (cls_dets2.size())[0]:
                    if cls_dets2[counterly][0] == outerx1[0]:
                       if cls_dets2[counterly][1] == outerx1[1]:
                          if cls_dets2[counterly][2] == outerx1[2]:
                             if cls_dets2[counterly][3] == outerx1[3]:
                                 if cls_dets2[counterly][4] == outerx1[4]:
                                    error = distancemin/1000
                                    cls_dets2[counterly][4] = cls_dets2[counterly][4] - error
                                    print("Actual Decrement")
                    counterly = counterly + 1
                print("Decrement")
            if distancemin < specialhypotenuse/2:
                counteras = 0
                while counteras < (cls_dets2.size())[0]:
                    if cls_dets2[counteras][0] == outerx1[0]:
                       if cls_dets2[counteras][1] == outerx1[1]:
                          if cls_dets2[counteras][2] == outerx1[2]:
                             if cls_dets2[counteras][3] == outerx1[3]:
                                if cls_dets2[counteras][4] == outerx1[4]:
                                   improvement = 1 - (2*distancemin)/specialhypotenuse
                                   cls_dets2[counteras][4] = cls_dets2[counteras][4] + improvement
                                   if cls_dets2[counteras][4] > 1:
                                      cls_dets2[counteras][4] = 1
                                   print("Actual Increment")
                    counteras = counteras + 1
                print("Increment")
            if distancemin <= 2 * specialhypotenuse:
                if distancemin >= specialhypotenuse/2:
                    print("Neither")
      counter = counter + 1
    return cls_dets2