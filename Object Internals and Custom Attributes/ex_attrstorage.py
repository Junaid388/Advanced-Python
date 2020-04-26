from vector import *

cv = ColoredVector(red = 23, green = 44, blue = 238, p= 9, q= 14)

cv.red # stored in a list at __dict__['color']

#cv.p # stored directly in __dict__
print(dir(cv))

print(cv) # look for color variable


# Method storage
v = Vector(x= 3, y=7)
print(v.__class__)

print(v.__class__.__dict__)  

print(v.__class__.__dict__['__repr__'](v))

#The __class__.__dict__ doesn't support item assignment as normal __dict__ so here how to assign a attribute
# Its like adding the attribute to class dictionary
setattr(v.__class__, 'a_vector_class_attribute', 5)

print(v.a_vector_class_attribute)

print(v.__class__.__dict__['__repr__'](v))

print(Vector.a_vector_class_attribute)

print(v)

