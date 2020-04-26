class Vector(object):
	"""docstring for Vector"""

	# Example for dunder dict
	# def __init__(self, x, y):
	# 	self.x = x
	# 	self.y =y

	# def __repr__(self):
	# 	return "{}({}, {})".format(self.__class__.__name__, self.x, self.y)
	
	# Example for private variable
	def __init__(self, **coords):
		private_coords = {'_' + k: v for k,v in coords.items()}
		self.__dict__.update(private_coords)

	def __getattr__(self, name):
		private_name = '_'+name
		try:
			return self.__dict__[private_name]
		except KeyError:  #when we request for a attribute which is not defined, Other with the __getattr will run in a loop 
			raise AttributeError("{!r} Object has no attribute {!r}".format(self.__class__,name))

	def __setattr__(self, name, value):
		raise AttributeError("Can't set attribute {!r}".format(name))

	def __delattr__(self, name): # stops deleting the attribute
		raise AttributeError("Cannot delete attribute {!r}".format(name))

	def __repr__(self):
		return "{}({})".format(self.__class__.__name__,
			', '.join("{k}={v}".format(
				k=k[1:],
				v=self.__dict__[k])
			for k in sorted(self.__dict__.keys())))

class ColoredVector(Vector):
	"""docstring for ColoredVector"""

	COLOR_INDEXES = ('red', 'green', 'blue')

	def __init__(self, red, green, blue, **coords):
		super(ColoredVector, self).__init__(**coords)
		self.__dict__['color'] = [red, green, blue]

	def __getattr__(self, name):
		try:
			channel = ColoredVector.COLOR_INDEXES.index(name)
		except ValueError:  
			raise super().__getattr__(name)
		else:
			return self.__dict__['color'][channel]

	def __setattr__(self, name, value):
		try:
			channel = ColoredVector.COLOR_INDEXES.index(name)
		except ValueError:  
			raise super().__getattr__(name, value)
		else:
			self.__dict__['color'][channel] = value