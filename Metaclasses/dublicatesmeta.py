class OneShotDict(dict):

	def __init__(self, name, existing=None):
		super().__init__()
		self._name = name
		if existing is not None:
			for k,v in existing:
				self[k] = v

	def __setitem__(self, key, value):
		if key in self:
			raise TypeError("Cannot reassign existing class attribute {!r} of {!r}".format(key, self._name))
		super().__setitem__(key, value)


class ProhibitDuplicateMeta(type):
	"""docstring for ProhibitDuplicateMeta"""

	@classmethod
	def __prepare__(mcs, name, bases):
		return OneShotDict(name)
		


class Dodge(object):
	"""docstring for Dodgy

	Dublicate clss attribute name are not flagged by python as erors
	The second definitin takes precedence
	becouse it overwrite the first entry in the name space dictionary
	as the class definition is processed"""
	def method(self):
		return 'First Definition'

	def method(self):
		return 'Second Definition'


# class Dodgy(metaclass = ProhibitDuplicateMeta):
# 	"""docstring for Dodgy"""
# 	def method(self):
# 		return 'First Definition'

# 	def method(self):
# 		return 'Second Definition'
		
		

if __name__ == '__main__':
	dodge = Dodge()
	print(dodge.method())

	d = OneShotDict('d')
	d['A'] = 65
	d['B'] = 66

	d['A'] = 32 # raises TypeError

	# Uncomment below Dodgy class to stop the reassignment of method
	

	#dodgy = Dodgy()  #raises TypeError
	#print(dodge.method())