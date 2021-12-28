# lists are mutable
colours = ["Red","Organge","Blue","Black"]
multiples = [ x*2 for x in range(11)] # list comprehension
length_coloura = [len(x) for x in colours]
print(length_coloura)
list_comprehension_conditional = [x for x in range(1,100) if x%11 == 0]
print(type(colours),len(colours),"Red" in colours)
print(colours,colours[-2:-1])
additional_colours = ["Blue","White","Orange"]
for color in additional_colours:
    if(color not in colours):
        colours.append(color)
print(colours)
colours.insert(0,"grey") # to insert at specific position
print(colours)
# if we use an index higher than current length it simply gets added at the end
colours.remove("grey") # removes first occurence of elemenet
print(colours)
colours.pop(1)
colours[1]="Orange"
print(colours)
for index,color in enumerate(colours):
    print("{} - {} ".format(index,color))#The enumerate object yields pairs containing a count (from start, which defaults to zero) and a value yielded by the iterable argument.

#enumerate is useful for obtaining an indexed list:
#    (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
def skip_elements(elements):
    	# code goes here
	new_elements = []
	for index,element in enumerate(elements):
		if index%2==0:
			new_elements.append(element)
	return new_elements

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

def full_emails(people):#people is list of tuple containing name and email need to conatin list containing name <email>
    final_list = []
    for email,name in people:
        final_list.append("{} <{}>".format(name,email))
    return final_list
print(full_emails([("vaibhav1karnal@gmail.com","Vaibhav Ahuja"),("ns1345@gmail.com","Nandan")]))

# tuple is immutable list kind of .... ("vaibhav","Ahuja")
# functions return tuple when returning many values as place or index has a meaning there
a,b,c = (1,"vaibhav",3) # (1,2,3) is tuple
tup = (1,2,3)
enumerate(tup)
