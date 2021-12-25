def greeting(name,department="na"):
    print("welcome " + str(name))
    print("department you belong to is " + str(department))
greeting("vaibahv","cse")
def area_triangle(height=0,base=0):
    return height*base/2
print(area_triangle(5,10))
def convert_sec(seconds):
    hours = seconds//3600
    minutes = (seconds - hours*3600)//60
    seconds = (seconds - hours*3600 - minutes*60)
    return hours,minutes,seconds
a,b,c = convert_sec(5000)
print(a,b,c)
re = greeting("hi") # re will have none datatype indicating nothing
print(re)