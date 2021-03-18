class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Figure:
	pass

class Circle(Figure):
	def __init__(self, x, y, radius):
		self.point = Point (x=x, y=y)
		self.radius = radius

	def perimeter(self):
		return self.radius * (2 * 3.14) 

	def area(self):
		return (self.radius ** 2) * 3.14 

class Tringle(Figure):
	def __init__(self, a, b, c):
		self.a = a
		self.b = b 
		self.c = c

	def perimeter(self):
		return self.a + self.b + self.c
		
	def area(self):
		return (self.a * self.b) / 2

class Square(Figure):
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def perimeter(self):
		return self.a * 2
		
	def area(self):
		return self.a * 4 



