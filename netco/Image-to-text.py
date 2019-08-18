import pytesseract  ####reading string from image (OCR library)
import  numpy as np ##numpy for shape
import cv2   #Computer vision library
import os    ##for remove image file which we edit during procedure


from PIL import Image, ImageDraw, ImageFont
#from difflib_data import *
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
###you need to install ocr and give path in program
try:
	image='dummy.jpg'
	print('Editing image for better OCR result..........')
	img = cv2.imread(image) #this will read an image and return an image as a numpy ndarray
	img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
	kernel = np.ones((1,1), np.uint8)
	img = cv2.dilate(img, kernel, iterations=1)
	img = cv2.erode(img, kernel, iterations=1)#it erodes away the boundaries of foreground object, all the pixels near boundary will be discarded depending upon the size of kernel.
	new_image = 'edited' + '_' + image  ###new image which we save during procedure
	cv2.imwrite(new_image, img)###Save a new edited image, to save an image. First argument is the file name, second argument is the image you want to save.
	read = pytesseract.image_to_string(new_image)  ####reading from new generated image
	print(read)  ##print result
	with open("taketext.txt", "w") as file:
		file.write(read)

	with open("enteredtext.txt", "w") as file:
		m="Name: Rukul Bhatt Gender: Female School: Children‘s Academy, GhaziabaD City: Ghaziabad roll no:	1691o9544 DOB: 01—09—1998 WHAT: Kyaaaa Where: kahaaaaaa Address: F—94, Sector— 9, New Vijay Nagar, Ghaziabad, Uttar Pradesh, India College: I.P.E.M. Group of Institutions College Id: 156923973 College Aff: C.C.S University, A.K.T.U, India"
		file.write(m)

	#with open('taketext.txt') as f1:
	 #   f1_text = f1.read()
	  #  if  f1_text=='g':
	   #     img = Image. new('RGB', (500, 500), color = 'white')
		#    fnt = ImageFont.truetype('C:\\Users\\Jyoti\\Desktop\\oppo\\font.ttf', 40)
		 #   d = ImageDraw. Draw(img)
		  #  d. text((65, 165), 'g' ,font=fnt, fill=(0, 0, 0))
		   # img. save('pil_text.png')
		#else:
		 #   img = Image. new('RGB', (500, 500), color = 'white')
		  #  fnt = ImageFont.truetype('C:\\Users\\Jyoti\\Desktop\\oppo\\font.ttf', 40)
		   # d = ImageDraw. Draw(img)
			#d. text((65, 165), f1_text ,font=fnt, fill=(255, 255, 0))
			#img. save('pil_text.png')
			#with open(filename) as f:

		#while True:
		 #   with open('taketext.txt') as f1:
		  #      f1_text = f1.read()
		   #     if 'q' in f1_text:
			#        img = Image. new('RGB', (500, 500), color = 'white')
			 #       fnt = ImageFont.truetype('C:\\Users\\Jyoti\\Desktop\\oppo\\font.ttf', 40)
			  #      d = ImageDraw.Draw(img)
			   #     d.text((65, 165), f1_text ,font=fnt, fill=(0, 0, 0))
				#    img.save('pqw_text.png')
				#else:
				 #   img = Image. new('RGB', (500, 500), color = 'white')
				  #  fnt = ImageFont.truetype('C:\\Users\\Jyoti\\Desktop\\oppo\\font.ttf', 40)
				   # d = ImageDraw. Draw(img)
					#d.text((65, 165), f1_text ,font=fnt, fill=(255, 255, 0))
				   # img.save('per_text.png')
		   # d = ImageDraw. Draw(img)
			#d. text((65, 165), f1_text ,font=fnt, fill=(255, 255, 0))
			#img. save('pil_text.png')





	#with open('enteredtext.txt') as f2:
		#f2_text = f2.read()

	#text1_lines = f1_text.splitlines()
	#text2_lines  = f2_text.splitlines()

	#img = Image.new(mode, size, color)
	#img = Image. new('RGB', (500, 500), color = 'white')
	#fnt = ImageFont.truetype('C:\\Users\\Jyoti\\Desktop\\oppo\\font.ttf', 40)
	#d = ImageDraw. Draw(img)
	#d. text((65, 165), f1_text,font=fnt, fill=(0, 0, 0))
	#img. save('pil_text.png')

	#for a in text1_lines[:]:
	 #   a= a.remove(" ")

  #  print(a)

	#diffList = list(diffInstance.compare(text1Lines, text2Lines))
	#print ('-'*50)
	#print ("Lines different in text1 from text2:")
	#for line in diffList:
	 #   if line[0] == '-':
	  #      print (line)
	#with open('taketext.txt', 'r') as file1:
	 #   with open('enteredtext.txt', 'r') as file2:
	  #      same = set(file1).intersection(file2)
	#print(same)


	#with open('some_output_file.txt', 'w') as file_out:
	 #   for line in same:
	  #      file_out.write(line)

	#encoded_image_path = text_to_image.encode("Hello World!", "image.png")

	#decoded_text = text_to_image.decode("image.png")

	#encoded_image_path = text_to_image.encode("enteredtext.txt", "image.png")

except Exception as e:
	print('Please provide proper name of the image')
	print(e)



#cv2.imshow('image name',image_var)display the image in a window and it receives as input the name of the window and the image we previously got with the imread function
#cv2.waitKey(0)execution of our program will block here until we press a key.After the user presses a key, we will assume the window with the image should be destroyed. To to so, we can call the destroyAllWindows function, which will destroy all the windows previously created [2]. Note that if we want to destroy a specific window, we can call the destroyWindow function, which receives as input the name of the window we want to destroy [2]. This second function is useful if we create multiple windows.
#cv2.destroyAllWindows()
#in imread()pass integers 1, 0 or -1 for Loads a color image,Loads image in grayscale mode,Loads image as such including alpha channel respectively.