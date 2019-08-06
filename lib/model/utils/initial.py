import numpy as np
# from scipy.misc import imread, imresize
import cv2
import torch
import math

def newfunction(f, x, i, a, k, y):
  a1, a2, a3, a4 = firstfunction(f, x, i, a)
  a5, a6, a7, a8 = firstfunction(i, a, k, y)
  return a1, a2, a4

def firstfunction(f, x, i, a):
  happyFace = torch.Tensor(([[0, 0]]))
  happyFaceX = 0
  happyFaceY = 0
  flipped = 0
  oddnum = 0
  cameramotion = 0
  plebian = 0
  pascalreturn1 = torch.Tensor(([0, 0, 0, 0], [0, 0, 0, 0]))
  pascalreturn2 = np.array([""])
  initia = torch.tensor(np.array([[0.0, 0.0]]))
  initiavel = torch.tensor(np.array([[0.0, 0.0]]))
  initiacel = torch.tensor(np.array([[0.0, 0.0]]))
  bridge = torch.tensor(np.array([[0.0, 0.0]]))
  lst = list(f)
  lst2 = list(i)
  f2 = 2
  i2 = 2
  
  angry = f.size
  reallyangry = i.size
  while lst[f2] != lst2[i2]:
       while lst[f2] < lst2[i2]:
          f2 = f2 + 1
       while lst[f2] > lst2[i2]:
          i2 = i2 + 1
  while (f2 < angry) & (i2 < reallyangry):
    g = torch.Tensor(([[0, 0]]))
    f3 = f2
    i3 = i2
    fcount = 0
    icount = 0
    if (f3 + 1) < angry:
       while lst[f3] == lst[f3 + 1]:
           fcount = fcount + 1
           f3 = f3 + 1
           if f3 >= angry - 1:
               break
    if (i3 + 1) < reallyangry:
       while lst2[i3] == lst2[i3 + 1]:
           icount = icount + 1
           i3 = i3 + 1
           if i3 >= reallyangry - 1:
               break
    if fcount > icount:
       flipped = 1
       lst3 = list(i)
       lst4 = list(f)
       igoogol = f2
       f2 = i2
       i2 = igoogol
       agoogol = x
       x = a
       a = agoogol
       fgoogol = icount
       icount = fcount
       fcount = fgoogol
    else:
       lst3 = list(f)
       lst4 = list(i)
    if (fcount % 2 == 0) & (fcount != 0):
       oddnum = 1 
    # At this point, x[f2] and a[i2] will store the starting location at which to compare
    # locations.
    fstored = fcount
    istored = icount
    mode = 0
    f4 = f2
    i4 = i2
    if oddnum == 1:
       fcount = fcount - 1
    size = 0
    while fcount >= 0:
       abba = torch.tensor(np.array([[0.0, 0.0]]))
       metallica = torch.tensor(np.array([[0.0, 0.0]]))
       labels1 = np.array([""])
       counter = 1
       while icount >= 0:
          midx = (x[f4][2] - x[f4][0])/2
          midy = (x[f4][3] - x[f4][1])/2
          temp1 = torch.Tensor(np.array([[midx, midy]]))
          abba = torch.cat((abba, temp1.double()), 0)
          midx2 = (a[i4][2] - a[i4][0])/2
          midy2 = (a[i4][3] - a[i4][1])/2
          temp2 = torch.Tensor(np.array([[midx2, midy2]]))
          metallica = torch.cat((metallica, temp2.double()), 0)
          lst99 = list(labels1)
          if flipped == 1:
             lst99.append(lst4[i4])
          else:
             lst99.append(lst3[f4])
          labels1 = np.asarray(lst99)
          deltax = midx2 - midx
          deltay = midy2 - midy
          if mode == 0:
              q = torch.Tensor(([[deltax, deltay]]))
              if flipped == 1:
                  q = q * -1
              g = torch.cat((g, q), 0)
              happyFace = torch.cat((happyFace, q), 0)
              size = size + 1
          else:
              g[counter][0] = g[counter][0] - deltax
              g[counter][1] = g[counter][1] - deltay
              counter = counter + 1
          icount = icount - 1
          i4 = i4 + 1
       icount = istored
       if mode == 0:
           mode = 1
           i4 = i2
       else:
           mode = 0
           i4 = i2
       fcount = fcount - 1
       f4 = f4 + 1
       temp3 = abba.size()
       temp4 = metallica.size()
       while (temp3[0] > 1) & (temp4[0] > 1):
          counter3 = 1
          counter4 = 1
          minimum = 10000
          minvx = 10000
          minvy = 10000
          pairx = 10000
          pairy = 10000
          pairx2 = 10000
          pairy2 = 10000
          storex = 10000
          storey = 10000
          labels3 = ""
          while counter3 < temp3[0]:
             while counter4 < temp4[0]:
                minx = (abba[counter3][0] - metallica[counter4][0])
                miny = (abba[counter3][1] - metallica[counter4][1])
                distance = math.sqrt(math.pow(deltax, 2) + math.pow(deltay, 2))
                if distance < minimum:
                    distance = minimum
                    pairx = abba[counter3][0]
                    # print(pairx)
                    pairy = abba[counter3][1]
                    # print(pairy)
                    minvx = minx
                    minvy = miny
                    pairx2 = metallica[counter4][0]
                    pairy2 = metallica[counter4][1]
                    storex = counter3
                    storey = counter4
                    labels3 = labels1[counter3]
                counter4 = counter4 + 1
             counter3 = counter3 + 1
             counter4 = 0
          initially = torch.tensor(np.array([[pairx, pairy]]))
          initia = torch.cat((initia, initially.double()), 0)
          initially2 = torch.tensor(np.array([[minvx, minvy]]))
          initiavel = torch.cat((initiavel, initially2.double()), 0)
          initially3 = torch.tensor(np.array([[pairx2, pairy2]]))
          bridge = torch.cat((bridge, initially3.double()), 0)

          lst1000 = list(pascalreturn2)
          lst1000.append(labels3)
          pascalreturn2 = np.asarray(lst1000)

          c = abba.numpy()
          d = metallica.numpy()
          e = np.array([[pairx, pairy]])
          red = np.array([labels3])
          f2000 = np.array([[pairx2, pairy2]])
          c = np.vstack(row for row in c if row not in e)
          d = np.vstack(row for row in d if row not in f2000)
          abba = torch.Tensor(c)
          metallica = torch.Tensor(d)
          labels1 = np.vstack(row for row in labels1 if row not in red)
          # abba = torch.cat([abba[0:counter3], abba[counter3+1:-1]])
          # abba = abba[abba!=counter3]
          # metallica = torch.cat([metallica[0:counter4], metallica[counter4+1:-1]])
          # metallica = metallica[metallica!=counter4]
          temp3 = abba.size()
          temp4 = metallica.size()
    f2 = f2 + fstored + 1
    i2 = i2 + istored + 1
    if flipped == 1:
        flipped = 0
        igoogol = f2
        f2 = i2
        i2 = igoogol
        agoogol = x
        x = a
        a = agoogol
    if (f2 < angry) & (i2 < reallyangry):
       while lst[f2] != lst2[i2]:
          while lst[f2] < lst2[i2]:
             f2 = f2 + 1
          while lst[f2] > lst2[i2]:
             i2 = i2 + 1
    counter2 = 1
    while counter2 < size:
      if g[counter2][0] < 5:
         if g[counter2][1] < 5:
            if (cameramotion == 1) | (plebian == 0):
               cameramotion = 1
               plebian = 1
               happyFaceXtemp = happyFace[counter2][0]
               happyFaceYtemp = happyFace[counter2][0] 
               if (happyFaceXtemp - happyFaceX < 5) | (happyFaceXtemp - happyFaceX > -5):
                   if (happyFaceYtemp - happyFaceY < 5) | (happyFaceYtemp - happyFaceY > -5):
                          happyFaceX = happyFaceXtemp
                          happyFaceY = happyFaceYtemp
                   else:
                          happyFaceX = (happyFaceX + happyFaceXtemp)/2
                          happyFaceY = (happyFaceY + happyFaceYtemp)/2
               else:
                   happyFaceX = (happyFaceX + happyFaceXtemp)/2
                   happyFaceY = (happyFaceY + happyFaceYtemp)/2
      counter2 = counter2 + 1
  if cameramotion == 1:
      initiavelsize = initiavel.size()
      countercounter = 0
      while countercounter < initiavelsize[0]:
           if (initiavel[countercounter][0] < 50) & (initiavel[countercounter][1] < 50):
               cameramotion = 0
           countercounter = countercounter + 1
  if cameramotion == 1:
      print("Camera motion detected")
      initiavelsize = initiavel.size()
      countercounter = 0
      while countercounter < initiavelsize[0]:
           silly = torch.tensor(np.array([[happyFaceX, happyFaceY]]))
           initiavel = initiavel - silly.double()
           countercounter = countercounter + 1
  print("Positions:", initia)
  print("Velocities:", initiavel)
  print("References:", bridge)
  print("Labels:", pascalreturn2)
  return initia, initiavel, bridge, pascalreturn2
