def decorator(func):
	def wrapper(*args):
		if args % 2 == 0:
			return True
		return False
		print (*args)


@decorator 
def foo (*args):
	return 

foo (1,2,3,4,5,6)