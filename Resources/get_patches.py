# import the necessary packages
import numpy as np
import argparse
import imutils
import glob
import cv2

##just include "from get_patches import get_patches" in the file where you want to use this function 
def get_patches(image):
	## template images
	## present in the dataset provided to you
	##change these paths accordingly
	template_paths = ["/home/shubham/Desktop/Images/2.png", "/home/shubham/Desktop/Images/3.png", "/home/shubham/Desktop/Images/4.png"]
	##stop : 2.png
	##right : 3.png
	##left : 4.png
	right = []
	left = []
	stop = []
	c=0
	for p in template_paths:
		# load the image image, convert it to grayscale, and detect edges
		c=c+1
		template = cv2.imread(p)
		template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
		template = cv2.Canny(template, 50, 200)
		#(tH, tW) = template.shape[:2]
		cv2.imshow("Template", template)
		template = imutils.resize(template, width=int(template.shape[1]*0.25))

		(tH, tW) = template.shape[:2]
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		found = None
		
		# loop over the scales of the image
		for scale in np.linspace(0.2, 1.0, 20)[::-1]:
			# resize the image according to the scale, and keep track
			# of the ratio of the resizing
			resized = imutils.resize(gray, width = int(gray.shape[1] * scale))
			r = gray.shape[1] / float(resized.shape[1])
			# if the resized image is smaller than the template, then break
			# from the loop
			if resized.shape[0] < tH or resized.shape[1] < tW:
				break

			# detect edges in the resized, grayscale image and apply template
			# matching to find the template in the image
			edged = cv2.Canny(resized, 50, 200)
			result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF_NORMED)
			(_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

			# if we have found a new maximum correlation value, then update
			# the bookkeeping variable
			if found is None or maxVal > found[0]:
				found = (maxVal, maxLoc, r)

		# unpack the bookkeeping varaible and compute the (x, y) coordinates
		# of the bounding box based on the resized ratio
		(maxVal, maxLoc, r) = found
		print maxVal
		(startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
		(endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))
		# draw a bounding box around the detected result and display the image
		cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
		# cv2.imwrite('boundingVisual/'+str(c)+'.png', image)	
		# cv2.imshow("Image", image)
		# cv2.waitKey(0)
		if c==1:
			stop=[maxVal, startX, startY, endX, endY]
		elif c==2:
			right=[maxVal, startX, startY, endX, endY]
		else:
			left=[maxVal, startX, startY, endX, endY]
	return stop,right,left