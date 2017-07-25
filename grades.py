#from numpy import *

# Each of our grades
kristen_grades = [90, 85, 100, 77, 94]
clarisse_grades = [96, 83, 89, 97, 86]
sapna_grades = [82, 91, 94, 87, 99]

# Class grade book
grade_book = [kristen_grades, clarisse_grades, sapna_grades]

'''
This is what our grade book looks like
[	[90, 85, 100, 77, 94]
	[96, 83, 89, 97, 86]
	[82, 91, 94, 87, 99] 

	'''	
def avg(num):
	return (num[0] + num[1] + num[2] + num[3] + num[4])/5

z = 0
for k in grade_book:
	h = avg(k)
	print(h) 
	z = z + h
j = z/3
print(j)

o = 0
for k in grade_book:
	v = (j - avg(k)) ** 2
	o = o + v
q = (o/3) ** .5
print(q)

# Traverse through the grade book and print all the indivdual grades


'''
for k in grade_book:
	print(k[0])
	print(k[1])
	print(k[2])
	print(k[3])
	print(k[4])
'''
# Extensions: Find the class average, median, and standard deviation
# (For the extentions google for hints!)

# Super extra extensions: calculate the student with highest/lowest average
