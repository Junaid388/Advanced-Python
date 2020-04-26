from vector import *

v= Vector(p=9, q=3)

print(v)

print(dir(v)) #as p is private we cannot access it directly

print(v.p)
print(v.q)

print(v._p)

#print(v.x) #Throws an error for creating an attribute

#del v.q

delattr(v, '_p')