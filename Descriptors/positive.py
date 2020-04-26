from weakref import WeakKeyDictionary

class Positive(object):
	"""docstring for Positive"""
	def __init__(self):
		self._instance_data = WeakKeyDictionary()

	def __get__(self, instance, owner):
		if instance is None: # Will helpful for getting attribute of class itself
			return self
		return self._instance_data[instance]

	def __set__(self, instance, value):
		if value <= 0:
			raise ValueError("Value {} is not Positive".format(value))
		self._instance_data[instance] = value

	def __delete__(self, instance):
		raise AttributeError ("Cannot delete attributes")
