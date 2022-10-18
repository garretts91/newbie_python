split_string = "This string has been\n split over \n several lines"
print(split_string)
tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string)

print('The Squish is "bork \'i\'n\'g"')
#or
print("The pet shop owner said \"no, no, hes a baby\"")
#or you can use three quotations in order to print escape characters
another_split_string="""This string has been
split
over
several
lines"""
print(another_split_string)
#the backslash can be used to escape the end of a line
exercise_split_string="Number 1 \t The Larch \nNumber 2 \t The Horse Chestnut"
print(exercise_split_string)
#You can escape backslashes by using another backslash
#You can also use r, but should only be used sparingly
print("C:\\Users\\grrtt\\coding\\escapeChars.py")