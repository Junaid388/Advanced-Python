from vector import *

v =Vector(5, 3)
print(v)
print(dir(v))
print(v.__dict__) #__dict__ is a dictionary, One which contains the name of the object attribute key and values of object attribute
print(type(v.__dict__))
print(v.__dict__['x'])
v.__dict__['x'] = 17
print(v.__dict__['x'])

del v.__dict__['x']

#print(v.x)

print('x' in v.__dict__)
print('y' in v.__dict__)

v.__dict__['z'] = 13
print(v.z)

# Similar use cases

print(getattr(v, 'y'))
print(hasattr(v, 'x'))
delattr(v , 'z')
setattr(v, 'x', 9)
print(v.x)