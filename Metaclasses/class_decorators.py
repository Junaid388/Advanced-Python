def my_class_decorator(cls):
	for name, attr in vars(cls).items():
		print(name)
	return cls

@my_class_decorator
class Temprature(object):
	"""docstring for Temprature"""
	def __init__(self, kelvin):
		self.kelvin = kelvin

	def get_kelvin(self):
		return self.kelvin

	def set_kelvin(self, value):
		self._kelvin = value
		