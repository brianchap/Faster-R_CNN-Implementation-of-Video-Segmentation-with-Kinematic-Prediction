
import numpy as np
import torch
# from scipy.misc import imread, imresize
import cv2
import math
#from models.components.proposal import scores
#from video import cls_dets

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
#   Create two arrays: prediction[] and actual[] 
#   Arrays contain the midpoint of the hypotenuse of the bounding box
#   Create variable confidence 
#   Using the kinematic prediction model, store the predicted location (midpoint of hypotenuse of bounding box) into prediction[] 
#   Using R-CNN, store ground truth location (midpoint of hypotenuse of bounding box) into actual[]
#   Create array error[]
#   For every value in prediction[] and actual[], calculate % error ( (actual - predicted value) / predicted value) ) and store into error[]
#   Average all the values in error[] to get one number (variable named avgerror for example)
#   Percentage of Confidence = 100 - (avgerror * 100) 
#   Scores to be altered are at line 24 of /models/components/proposal.py.

##############THIS FUNCTION IS BEING EDITED AT THE MOMENT##############



oldmidx = -1
oldmidy = -1

olddmidx = -1
olddmidy = -1

vx = -1
vy = -1

oldvx = 0
oldvy = 0

ax = -1
ay = -1

objtru = -1

t = 1

def oldfunction(interval, pascal_classes, cls_dets, pascalreturn3):
    
    global oldmidx, oldmidy, olddmidx, olddmidy, vx, vy, oldvx, oldvy, ax, ay, objtru, t

    # predicted locations of all subjects after N frames
    num_predict = torch.zeros(len(list(pascal_classes)))
    class_predict = pascalreturn3
    N = interval
    

    x1 = cls_dets[0][0]
    y1 = cls_dets[0][1]
    x2 = cls_dets[0][2]
    y2 = cls_dets[0][3]
    prob = cls_dets[0][4]
    center = torch.tensor(np.array([[0.0, 0.0]]))

    midx = (x1 + x2)/2
    midy = (y1 + y2)/2
    print ("mid =")
    print (midx)
    print (midy)
    temp = torch.Tensor(np.array([[midx, midy]]))
    center = torch.cat((center, temp.double()), 0)  

    if (oldmidx == -1) | (oldmidy == -1):
        vx = -1
        vy = -1
        objtru = -1
    else:
        vx = (midx - oldmidx)
        vy = (midy- oldmidy)
        objtru = 1
        print ("v =")
        print (vx)
        print (vy)

    if ((oldvx == -1) and (oldvy == -1)) or ((vx == -1) and (vy == -1)):
        ax = 0
        ay = 0
        print ("a =")
        print (ax)
        print (ay)
    else:
        ax = (vx - oldvx)
        ay = (vy - oldvy)
        print ("a =")
        print (ax)
        print (ay)


    if (objtru == 1):
    
        for i in range(len(list(pascal_classes))):
            print ("wow")
            print (pascal_classes[i])
            flag = 0
            for j in range(len(list(pascalreturn3))):
                print ("whoa")
                print (pascalreturn3[j])
                if pascalreturn3[0:i] == pascal_classes[0:j]:
                    print ("nice")
                    flag = 1
                    predx = (ax/2)*(t**2) + oldvx*(t) + oldmidx
                    predy = (ay/2)*(t**2) + oldvy*(t) + oldmidy
                    print ("pred =")
                    print (predx)
                    print (predy)
                    dist = math.sqrt(((predx - midx)**2) + ((predy - midy)**2))
                    print ("dist =")
                    print (dist)
                    if flag == 1:
                        dist_min = dist
                        flag = 0
                        num_predict[i] = j
                    if dist < dist_min:
                        num_predict[i] = j
                    dist = dist_min
        objtru = -1
    

    # g = cls_dets.cpu().size()
    # h = g[0]
    # while h > 0:
    #     lst.append(pascal_classes[j])
    #     h = h - 1
    
    #pascal_class_tensor = torch.from_numpy(pascal_class)
    # pascal_predict = pascal_initial + pascalreturn1 * N
    # g = 9.8
    # pascal_predict[:,2] = pascal_class_tensor + (0.5 * g * N**2)
    # pascal_predict[:,4] = pascal_class_tensor + (0.5 * g * N**2)
    # class_predict = pascalreturn2
    # num_predict = torch.zeros(len(list(pascalreturn2)))
    # num_gt = torch.zeros(len(list(cls_dets)))
    # dist = torch.zeros(len(list(pascalreturn2)))
                     
    # for i in len(list(cls_dets)):
    # # calculate the distance of the movement and find out the minium one
    #     flag = 0 # for initializing the minimum distance
    #     num_gt[i] = i
    #     for j in len(list(pascalreturn2)):
    #         if cls_dets[i] == pascalreturn2[j]:
    #             flag = 1
    #             bboxcenter1_x = 0.5 * (pascal_class_tensor[n,1] + pascal_class_tensor[n,3])
    #             bboxcenter1_y = 0.5 * (pascal_class_tensor[n,2] + pascal_class_tensor[n,4])
    #             bboxcenter2_x = 0.5 * (pascal_predict[n,1] + pascal_predict[n,3])
    #             bboxcenter2_y = 0.5 * (pascal_predict[n,2] + pascal_predict[n,4])
    #             # calculating the distance of the objects between the predict location and current location
    #             dist = sqrt(square(bboxcenter2_x - bboxcenter1_x) + square(bboxcenter2_x - bboxcenter2_x))
    #             # initializing the minimum distance
    #             if flag == 1:
    #                 dist_min = dist
    #                 flag = 0
    #                 num_predict[i] = j
    #             #upgrade the minimum distance of current object
    #             if dist < dist_min:
    #                 num_predict[i] = j
    #             dist[i] = dist_min
    #         j = j + 1
    #     i = i + 1
                        
    # #calculate the hypotenuse of the bounding box
    # for m in len(list(num_gt)):
    #     hypo = sqrt(square(pascal_class[i,3] - pascal_class[i,1]) + square(pascal_class[i,4] - pascal_class[i,2]))
    #     if dist[m] > 2 * hypo:
    #         #score[i] = score - n
    #         print ("!")
    #     if dist[m] < 0.5 * hypo:
    #         #score[i] = score - n
    #         print ("!")


    oldmidx = midx
    oldmidy = midy

    olddmidx = oldmidx
    olddmidy = oldmidy

    oldvx = vx
    oldvy = vy

    return center, class_predict
    #return 0, 0