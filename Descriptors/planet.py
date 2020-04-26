from positive import *

class Planet(object):
	"""docstring for Planet"""
	def __init__(self, name, radius_metres, mass_kilograms, orbital_period_seconds, surface_temprature_kelvin):
		self.name = name
		self.radius_metres = radius_metres
		self.mass_kilograms = mass_kilograms
		self.orbital_period_seconds = orbital_period_seconds
		self.surface_temprature_kelvin = surface_temprature_kelvin

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		if not value:
			raise ValueError("Cannot set empty Planet.name")
		self._name = value

	radius_metres = Positive()
	mass_kilograms = Positive()
	orbital_period_seconds = Positive()
	surface_temprature_kelvin = Positive()


def main():
	
	mercury = Planet("Mercury", 24, 3.3, 7.6, 3)

	venus = Planet("Venus", 60, 4.8, 1.9, 7)

	earth = Planet("Earth", 63, 5.9, 3.1, 2)

	mars = Planet("Mars", 33, 6.4, 5.9, 2)

	return mercury, venus, earth, mars

if __name__ == '__main__':
	mercury, venus, earth, mars = main()
	print(mars.radius_metres)


	# The new descriptor approah will be similar to
	# m = pluto.mass_kilograms.      m = Positive.__get__(self, pluto, Planet)
	# pluto.mass_kilograms = m.      Positive.__set__(self, pluto, m)

	# @property
	# def radius_metres(self):
	# 	return self._radius_metres

	# @radius_metres.setter
	# def radius_metres(self, value):
	# 	if value <= 0:
	# 		raise ValueError("radius_metres value {} is not positive.".format(value))
	# 	self._radius_metres = value

	# @property
	# def mass_kilograms(self):
	# 	return self._mass_kilograms
	
	# @mass_kilograms.setter
	# def mass_kilograms(self, value):
	# 	if value <= 0:
	# 		raise ValueError("mass_kilograms value {} is not positive.".format(value))
	# 	self._mass_kilograms = value

	# @property
	# def orbital_period_seconds(self):
	# 	return self._orbital_period_seconds

	# @orbital_period_seconds.setter
	# def orbital_period_seconds(self, value):
	# 	if value <= 0:
	# 		raise ValueError("orbital_period_seconds value {} is not positive.".format(value))
	# 	self._orbital_period_seconds = value

	# @property
	# def surface_temprature_kelvin(self):
	# 	return self.surface_temprature_kelvin

	# @surface_temprature_kelvin.setter
	# def surface_temprature_kelvin(self, value):
	# 	if value <= 0:
	# 		raise ValueError("surface_temprature_kelvin value {} is not positive.".format(value))
	# 	self._surface_temprature_kelvin = value
	
	
		