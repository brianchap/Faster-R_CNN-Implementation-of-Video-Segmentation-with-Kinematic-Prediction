# Faster R-CNN Implementation of Video Segmentation with PyTorch 1.0

This is the first-known implementation of R-CNN-based video segmentation that is PyTorch 1.0 compatible (stable versions included).

Ensure that your system has PyTorch, Python, and numpy 1.16.1+ already installed.

Execute pip install -r requirements.txt

Execute python setup.py build develop from the lib directory

Add the file at https://www.dropbox.com/s/6ief4w7qzka6083/faster_rcnn_1_6_10021.pth?dl=0 to models/res101/pascal_voc

Add the file at https://www.dropbox.com/s/4v3or0054kzl19q/faster_rcnn_1_7_10021.pth?dl=0 to models/res101/pascal_voc

To test an image, execute the following: python demo.py --net res101 --checksession 1 --checkepoch 7 --checkpoint 10021 --load_dir ./models (with the images in an images folder in the root directory)

To test a video, execute the following: python video.py --net res101 --checksession 1 --checkepoch 7 --checkpoint 10021 --load_dir ./models --video XXX (where XXX is the name of the video with extension included; videos should be located in a video folder in the root directory)

![Sample Frame No. 1](/samples/Picture2.jpg)

![Sample Frame No. 2](/samples/Picture3.jpg)

![Sample Frame No. 3](/samples/Picture4.jpg)
