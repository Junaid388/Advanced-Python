class MetaA(type):
	pass


class MetaB(type):
	pass

class MetaC(MetaA, MetaB):
	pass



class A(metaclass = MetaA):
	pass


class B(metaclass = MetaB):
	pass


class D(A):
	pass

# class C(A,B):
# 	pass

	
class C(A,B, metaclass = MetaC):
	pass

if __name__ == '__main__':
	print(type(D))		# The metaclass of d is metaclass A which is inherited from its regular base class A. metaclasses are inherited

	print(type(C))