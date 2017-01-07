# import the necessary packages
import numpy as np
import cv2

# load the image, clone it for output, and then convert it to grayscale
for x in range(1, 101):
	if (x < 10):	
		#print "000%d.jpg" % (x)
		temp = "input/000%d.jpg" % (x)
		image = cv2.imread(temp)
	elif (x == 100):
		#print "0%d" % (x)
		temp = "input/0%d.jpg" % (x)
		image = cv2.imread(temp)
	else:
		#print "00%d" % (x)
		temp = "input/00%d.jpg" % (x)
		image = cv2.imread(temp)

	#image = cv2.imread("0001.jpg")

	output = image.copy()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	#clean the image using otsu method
	ret,th = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

	# assign the kernel size
	kernel = np.ones((5,5),'uint8')

	# perform opening operation
	opening = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)
	
	#contours,hierarchy = cv2.findContours(opening, 1, 2)	
	
	# loop the csv file for all the center of the circles
	file = open("fields39.csv", "rb") 
	for line in file:
		points = line.split()
		#print th[189,600]
		#print points[0]
		#print points[1]
		# 1st Column
		left = int(points[0]) - 8
		top = int(points[1]) - 8
		right = int(points[0]) + 8
		bottom = int(points[1]) + 8
		
		width = right - left
		height = bottom - top	
		rect = opening[top:bottom, left:right]
		meanIntensity = rect.mean()			
		#print meanIntensity
		if(meanIntensity < 69):
			#print "pasok dito s blue"
			cv2.rectangle(output, (left, top), (right, bottom), (255, 0, 0), 2)	
		elif(meanIntensity < 135 and meanIntensity > 69):
			cv2.rectangle(output, (left, top), (right, bottom), (0, 0, 255), 2)
		else:
			cv2.rectangle(output, (left, top), (right, bottom), (0, 255, 0), 2)

		# 2nd Column
		left = int(points[2]) - 8
		top = int(points[3]) - 8
		right = int(points[2]) + 8
		bottom = int(points[3]) + 8
		
		width = right - left
		height = bottom - top	
		rect = opening[top:bottom, left:right]
		meanIntensity = rect.mean()			
		#print meanIntensity
		if(meanIntensity < 69):
			#print "pasok dito s blue"
			cv2.rectangle(output, (left, top), (right, bottom), (255, 0, 0), 2)	
		elif(meanIntensity < 135 and meanIntensity > 69):
			cv2.rectangle(output, (left, top), (right, bottom), (0, 0, 255), 2)
		else:
			cv2.rectangle(output, (left, top), (right, bottom), (0, 255, 0), 2)
		
		# 3rd Column
		left = int(points[4]) - 8
		top = int(points[5]) - 8
		right = int(points[4]) + 8
		bottom = int(points[5]) + 8
		
		width = right - left
		height = bottom - top	
		rect = opening[top:bottom, left:right]
		meanIntensity = rect.mean()			
		#print meanIntensity
		if(meanIntensity < 69):
			#print "pasok dito s blue"
			cv2.rectangle(output, (left, top), (right, bottom), (255, 0, 0), 2)	
		elif(meanIntensity < 135 and meanIntensity > 69):
			cv2.rectangle(output, (left, top), (right, bottom), (0, 0, 255), 2)
		else:
			cv2.rectangle(output, (left, top), (right, bottom), (0, 255, 0), 2)
		
			
		# 4th Column
		left = int(points[6]) - 8
		top = int(points[7]) - 8
		right = int(points[6]) + 8
		bottom = int(points[7]) + 8
		
		width = right - left
		height = bottom - top	
		rect = opening[top:bottom, left:right]
		meanIntensity = rect.mean()			
		#print meanIntensity
		if(meanIntensity < 69):
			#print "pasok dito s blue"
			cv2.rectangle(output, (left, top), (right, bottom), (255, 0, 0), 2)	
		elif(meanIntensity < 135 and meanIntensity > 69):
			cv2.rectangle(output, (left, top), (right, bottom), (0, 0, 255), 2)
		else:
			cv2.rectangle(output, (left, top), (right, bottom), (0, 255, 0), 2)

		# 5th Column
		left = int(points[8]) - 8
		top = int(points[9]) - 8
		right = int(points[8]) + 8
		bottom = int(points[9]) + 8
		
		width = right - left
		height = bottom - top	
		rect = opening[top:bottom, left:right]
		meanIntensity = rect.mean()			
		#print meanIntensity
		if(meanIntensity < 69):
			#print "pasok dito s blue"
			cv2.rectangle(output, (left, top), (right, bottom), (255, 0, 0), 2)	
		elif(meanIntensity < 135 and meanIntensity > 69):
			cv2.rectangle(output, (left, top), (right, bottom), (0, 0, 255), 2)
		else:
			cv2.rectangle(output, (left, top), (right, bottom), (0, 255, 0), 2)

		# 6th Column
		left = int(points[10]) - 8
		top = int(points[11]) - 8
		right = int(points[10]) + 8
		bottom = int(points[11]) + 8
		
		width = right - left
		height = bottom - top	
		rect = opening[top:bottom, left:right]
		meanIntensity = rect.mean()			
		#print meanIntensity
		if(meanIntensity < 69):
			#print "pasok dito s blue"
			cv2.rectangle(output, (left, top), (right, bottom), (255, 0, 0), 2)	
		elif(meanIntensity < 135 and meanIntensity > 69):
			cv2.rectangle(output, (left, top), (right, bottom), (0, 0, 255), 2)
		else:
			cv2.rectangle(output, (left, top), (right, bottom), (0, 255, 0), 2)

		# 7th Column
		left = int(points[12]) - 8
		top = int(points[13]) - 8
		right = int(points[12]) + 8
		bottom = int(points[13]) + 8
		
		width = right - left
		height = bottom - top	
		rect = opening[top:bottom, left:right]
		meanIntensity = rect.mean()			
		#print meanIntensity
		if(meanIntensity < 69):
			#print "pasok dito s blue"
			cv2.rectangle(output, (left, top), (right, bottom), (255, 0, 0), 2)	
		elif(meanIntensity < 135 and meanIntensity > 69):
			cv2.rectangle(output, (left, top), (right, bottom), (0, 0, 255), 2)
		else:
			cv2.rectangle(output, (left, top), (right, bottom), (0, 255, 0), 2)


	# show and write the output image
	#cv2.imshow("output", output)
	#cv2.imshow("opening", opening)
	
	
	if (x < 10):	
		print "000%d" % (x)
		temp2 = "output/000%d.jpg" % (x)
		cv2.imwrite(temp2, output)
	elif (x == 100):
		print "0%d" % (x)
		temp2 = "output/0%d.jpg" % (x)
		cv2.imwrite(temp2, output)
	else:
		print "00%d" % (x)
		temp2 = "output/00%d.jpg" % (x)
		cv2.imwrite(temp2, output)
	cv2.waitKey(0)
