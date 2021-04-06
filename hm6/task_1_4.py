class Car:
	def __init__(self, mark, model, year, speed = 0):
		self.__mark = 'a'
		self.__model = 'b'
		self.__year = 'c'
		self.__speed = 0

	def racing(self):
		return self.__speed + 5

	def drop(self):
		try:
			if self.__speed > 0:
				return self.__speed - 5

			else:
				raise ValueError

		except ValueError:
			print ('скорость ниже нуля')

	def stop(self):
		return self.__speed 

	def show(self):
		print (self.__speed) 

	def change(self):
		return self.__speed * -1 

