
import numpy as np
# from scipy.misc import imread, imresize
import cv2
from models.components.proposal import scores

# Parameters are as follows:
#   N:The interval between the extracted frames for correction
#   pascal_initial: The initial location of all subjects detected in the first frame
#   pascal_class: The locations of all subjects detected in the current frame
#   cls_dets: The class labels of all subjects detected in the current frame
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
def oldfunction(interval, pascal_initial, pascal_class, cls_dets, pascalreturn1, pascalreturn2):
    
    # predicted locations of all subjects after N frames
    pascal_predict = pascal_initial + pascalreturn1 * N
    g = 9.8
    pascal_predict[:,2] = pascal_class + 0.5 * g * square(N) 
    pascal_predict[:,4] = pascal_class + 0.5 * g * square(N) 
    
    class_predict = pascalreturn2
    num_predict = torch.zeros(len(list(pascalreturn2)))
    num_gt = torch.zeros(len(list(cls_dets)))
    dist = torch.zeros(len(list(pascalreturn2)))
                     
    for i in len(list(cls_dets)):
    # calculate the distance of the movement and find out the minium one
        flag = 0 # for initializing the minimum distance
        num_gt[i] = i
        for j in len(list(pascalreturn2)):
            if cls_dets[i] == pascalreturn2[j]:
                flag = 1
                bboxcenter1_x = 0.5 * (pascal_class[n,1] + pascal_class[n,3])
                bboxcenter1_y = 0.5 * (pascal_class[n,2] + pascal_class[n,4])
                bboxcenter2_x = 0.5 * (pascal_predict[n,1] + pascal_predict[n,3])
                bboxcenter2_y = 0.5 * (pascal_predict[n,2] + pascal_predict[n,4])
                # calculating the distance of the objects between the predict location and current location
                dist = sqrt(square(bboxcenter2_x - bboxcenter1_x) + square(bboxcenter2_x - bboxcenter2_x))
                # initializing the minimum distance
                if flag == 1:
                    dist_min = dist
                    flag = 0
                    num_predict[i] = j
                #upgrade the minimum distance of current object
                if dist < dist_min:
                    num_predict[i] = j
                dist[i] = dist_min
            j = j + 1
        i = i + 1
                        
    #calculate the hypotenuse of the bounding box
    for m in len(list(num_gt)):
        hypo = sqrt(square(pascal_class[i,3] - pascal_class[i,1]) + square(pascal_class[i,4] - pascal_class[i,2]))
        if dist[m] > 2 * hypo:
            #score[i] = score - n
        if dist[m] < 0.5 * hypo:
            #score[i] = score - n
