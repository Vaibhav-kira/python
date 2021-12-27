# strings are immutable objects
str1 = "Vaibhav"
print(str1*2)
print("B" in str1)
print(str1[0])
print(str1[0:6]) # six will not bi included
print(str1[0:]) # print till end
print(str1[:5]) # till str[4] from start
print(str1[::-1]) # reverse
print(str1.count("a"))
multi_line_str = """This is a multi line string (line 1)
This is a multi line string(line 2)"""
print(multi_line_str)
#negitive indexing is also possible
print(str1[-7:6]) # or str[-7:-1]
print(str1.upper()) # return copy of string in upper case
print(str1.capitalize()) # first char upper else lower
print(str1.isalnum()) # return true if string is alpha numetric i.e does not contail specisal char
# must have atleast one char
print(multi_line_str.split()) ## returns list
###sep
  ##The delimiter according which to split the string. None (the default value) means split according to any whitespace, and discard empty strings from the result.
##maxsplit
  ##Maximum number of splits to do. -1 (the default value) means no limit.###
str2 = "Hellow-world-vaibhav-this-side"
print(str2.split('-')) ## returns list
print(str2.replace("-"," ")) ## replaces - with space( ) returns string
str3 = " Vaibhav "
print(str3.strip()) #Return a copy of the string with leading and trailing whitespace removed.
#find()	Searches the string for a specified value and returns the position of where it was found
#index()	Searches the string for a specified value and returns the position of where it was found
# formatting 
v1 = 56.2365
v2 = 22.2354
v3 = v1/v2
print("whe {} is divided by {} result is {} ".format(v1,v2,v3))#used to include non string in string
# for formating the expression
print("whe {:.2f} is divided by {:.2f} result is {:.2f} ".format(v1,v2,v3))#used to include non string in string
# very important up ....
