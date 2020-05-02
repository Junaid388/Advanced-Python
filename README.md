# Advanced-Python

# Advanced Flow Control

It consist of differnet types of looping control flow in Python

1. While - Else
2. For - Else
3. Try - Except - Else
4. Switch Emulation
5. Implemetation of single dispatcher


# Internal object representation

1. The __dict__ dictionary
2. Manipulating __dict__
3. Faking attributes
4. Save space with __slots__


# Descriptors

1. properties
2. custom descriptor
3. data and no data descriptors (data descriptors contains get, set and delte while non-data descriptors only contains get like read only object)

# Class Defination

class Widget:
    pass


name = 'Widget'
metaclass = type
bases = ()
kwargs = {}
namespace = metaclass.__prepare__(name, bases, **kwargs)
Widget = metaclass.__new__(metaclass, name, bases, namespace, **kwargs)
metaclass.__init__(Widget, name, bases, namespace, **kwargs) 


# Meta classes
1. All classes have metaclass ehich is the type of class object
2. The default metaclss is type
3. Metaclasses convert parsed class namespaces into a class objects
4. 

