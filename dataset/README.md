# Dataset In Progress

GUYS, WE ARE MOST LIKELY NOT USING A FASTER R-CNN ARCHITECTURE IN THE FUTURE (WE MIGHT, BUT WE NEED TO IMPROVE PAST ~3 SPF TO SOMETHING LIKE 4 FPS)! CHENXI AND I HAVE SWITCHED TO A SIAMESE NETWORK-BASED ALGORITHM THAT CAN ACHIEVE ~40 FPS WITHOUT PHYSICS. I HAVE ASKED ACHUTA TO MOVE THE DEADLINE TO OCTOBER, BUT CHENXI IS CURRENTLY WORKING ON A DATASET THAT IS OVER 1 TB LARGE (IMAGENET VID).

SOME THOUGHTS:
   - CHENXI WILL BE LEAVING ON SEPTEMBER 15. THE ONLY COMPUTER THAT WORKS WITH THE ALGORITHM IS THE ONE IN LAB. YOU CAN USE TEAMVIEWER TO 
     ACCESS THE COMPUTER REMOTELY, BUT KNOW THAT CHENXI WILL BE WORKING EXTENSIVELY ON IT UNTIL THE 15TH. AFTER THE 15TH, SHE WOULD STILL LIKE 
     TO WORK ON THE PROJECT, SO PLEASE KNOW THIS.
   - I WILL BE LEAVING ON AUGUST 31 TO A PLACE WITH LIMITED WIFI. I WILL CONTINUE SENDING E-MAILS FOR UPDATES AND ASSISTING WITH MERGING THE 
     PHYSICS MODEL INTO THE ALGORITHM. THE MODEL CAN BE FOUND HERE: https://github.com/STVIR/pysot. I WILL BE BACK ON SUNDAY, SEPTEMBER 22.
   - KEVIN WILL BE ARRIVING ON CAMPUS IN EARLY SEPTEMBER.
   
JUST SOME FRIENDLY NEWS. - Brian

As of right now, we are working to create an ideal dataset for the Faster R-CNN with Kinematic Prediction system to run on. 
This will be another training model for the R-CNN to train on in order to accurately track and predict motion of objects using kinematics. 

Within this dataset, we have included vertical drops, tosses, depth transformations away from the camera, and linear motion down a ramp such as slides and rolls of objects. We are currently working toward adding more objects and annotating current data with bounding boxes for training. 

To extend the dataset:

1) Film easily identifiable, isolated objects under motion (e.g. freefall) 
    i) For better data, film with at least 120 fps
2) Annotate each video by manually applying a boundary box and label for the object each frame
