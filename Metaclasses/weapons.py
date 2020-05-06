class SwordMeta(type):
	"""docstring for ClassName"""
	def __instancecheck__(cls, instance):
		return cls.__subclasscheck__(type(instance))

	def __subclasscheck__(cls, sub):
		return (hasattr(sub, 'swipe') and callable(sub.swipe) and hasattr(sub, 'sharpen') and callable(sub.sharpen))
		

class Sword(metaclass = SwordMeta):
	
	def thrust(self):
		print("Thrusting....")


class BroadSword:

	def swipe(self):
		print('Swoosh!')

	def sharpen(self):
		print('Shink!')


class SamuraiSword:

	def swipe(self):
		print('Slice!')

	def sharpen(self):
		print('Shink!')

class Rifle:

	def fire(self):
		print('Bang!')


if __name__ == '__main__':
	print(issubclass(BroadSword, Sword))
	print(issubclass(SamuraiSword, Sword))
	print(issubclass(Rifle, Sword))

	samurai_sword = SamuraiSword() 
	print(isinstance(samurai_sword, Sword)) # will result in False if __instancecheck__() is not implemented


	# Non-transitive Subclass relationship

	from collections.abc import Hashable

	print(issubclass(object, Hashable))
	print(issubclass(list, object))
	print(issubclass(list, Hashable))	# no transitive relation as Hashable-->object-->list

	# further investigation
	print(object.__hash__)
	print(list.__hash__) # List class set __hash__ to none

	print("-------------------------------")
	# further explanation
	broad_sword = BroadSword()
	print(isinstance(broad_sword, Sword))
	print(broad_sword.swipe())
	print(broad_sword.thrust()) # will result in error