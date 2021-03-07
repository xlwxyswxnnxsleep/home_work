def decorator(func):
	import time 
	def wrapper(*args, **kwargs):
		start = time.time()
		res = func(*args, **kwargs)
		end = time.time()
		print (*args, *kwargs)
		print ('Время выполнения:', (end-start))
		return res
	return wrapper