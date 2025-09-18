from itertools import count
import cv2
import numpy as np
import glob
# Import et lecture des images

image_paths = glob.glob("D:\Python_Project\Image_Stitching\img\*.jpg")
images = [cv2.imread(image) for image in glob.glob("D:\Python_Project\Image_Stitching\img\*.jpg")]

# Affichage des images selectionnees
count = 0
for image in images:
    cv2.imshow(f"Image{count}", image)
    count=count+1
    cv2.waitKey(0)

imagestitcher = cv2.Stitcher_create()

error, stitched_img =imagestitcher.stitch(images)

if not error:
    cv2.imwrite("stitchedsortie.jpg", stitched_img)
    cv2.imshow("Stitched_im", stitched_img)
    cv2.waitKey(0)