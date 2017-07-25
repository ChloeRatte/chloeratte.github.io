from PIL import Image

# RGB values for recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

# Import image
# change IMAGENAME to the path on your computer to the image 
# you're using'''
z = input("What picture?")

my_image = Image.open(z) 
print(my_image.size[0]*my_image.size[1])

# each pixel is represented in the form 
# (red value, green value, blue value, transparency)
image_list = my_image.getdata()  

# Turns the sequence above into a list, it can be iterated through
# in a loop
image_list = list(image_list)
print("Size: ")
print(len(image_list))



# list that will hold the pixel data for the new image
recolored = [] 
#**************************************************#
#**************************************************#

#YOUR CODE to loop through the original list of pixels and 
# build a new list based on intensity should go here.
index=0
for a in image_list:
	c = a[0] + a[1] + a[2]
	if c < 182:
		recolored.append(darkBlue)
	elif c < 364:
		recolored.append(red)
	elif c < 546:
		recolored.append(lightBlue)
	else:
		recolored.append(yellow)



#**************************************************#
#**************************************************#
# Create a new image using the recolored list. Display and save 
# the image.

# Creates a new image that will be the same size as the original
new_image = Image.new("RGB", my_image.size)

# Adds the data from the recolored list to the image
new_image.putdata(recolored)

# Opens the new image on the screen
new_image.show() 

# Saves the new image as "recolored.jpg"
new_image.save("recolored.jpg", "jpeg") 