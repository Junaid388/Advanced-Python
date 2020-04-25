def is_comment(item):
	return isinstance(item, str) and item.startswith('#') #is instance check the give item is a string or not

def execute(program):
	""" Execute a stack program.

	Args:
		program: Any stack-like containting where is item in the stack
			is a collable operators or non-collable opernds. The top-most
			items on the stack may be strings beginning with '#' for
			the purpose of documentation. Stack-like means support for:

				item = stack.pop()	# Remove and return the top item
				stack.append(item)	# Push an item to the top
				if stack:			# False in a boolean context when empty
	"""
	# Find the start of the 'program' by skipping
	# any item which is a comment
	while program:
		item =program.pop()
		if not is_comment(item):
			program.append(item)
			break
	else:	#nobreak
		print("Empty program")
		return

	# Evalute the program
	pending = []
	while program:
		item = 	program.pop()
		if callable(item):
			try:
				result = item(*pending) #*pending gives items in the pending list item(5,2)
			except Exception as e:
				print("Error: ",e)
				break
			program.append(result)
			pending.clear()
		else:
			pending.append(item)
	else:	#nobreak
		print('Program Succesful.')
		print('Result: ',pending)


	print('Finished')

if __name__ == '__main__':
	import operator

	program = list(reversed((
		"# A short stack program to add",
		"# and multiply some constants",
		5,
		2,
		operator.add,
		3,
		operator.mul)))

	execute(program)