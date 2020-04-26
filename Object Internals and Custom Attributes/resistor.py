class Resistor(object):
	"""docstring for Resistor"""

	__slots__ = ['resistance_ohms', 'tolerance_percent', 'power_watts']

	def __init__(self, resistance_ohms, tolerance_percent, power_watts):
		self.resistance_ohms = resistance_ohms
		self.tolerance_percent = tolerance_percent
		self.power_watts = power_watts
		

r10 = Resistor(10, 5, 25)
print(r10.tolerance_percent)


# Check the getsize of object before using __slots__

import sys

print(sys.getsizeof(r10))

# The downsize of __slots__ we no longer add dynamic attributes to instance of Resister
# this is becouse the internal structure of Resister no longer contains __dict__
# Use __slots_wisely