from PIL import Image

# RGB values for recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

darkRed = (39,0,1)
tanIsh = (29,19,18)
magEnta = (115,20,63)
pinkIdk = (190,168,162)

l = input("Original or Magenta Set?")
if l != "Original" and l != "Magenta Set":
	print("Please type Original or Magenta Set")
elif l == "Original":
	useSet = [darkBlue, red, lightBlue, yellow]
else:
	useSet = [darkRed, tanIsh, magEnta, pinkIdk]

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
		recolored.append(useSet[0])
	elif c < 364:
		recolored.append(useSet[1])
	elif c < 546:
		recolored.append(useSet[2])
	else:
		recolored.append(useSet[3])



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