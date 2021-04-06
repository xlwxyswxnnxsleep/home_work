class Iterator:
	def __init__(self, collection, cursor =-1):
		self.cursor = cursor
		self.collection = collection

	def __iter__(self):
		return self

	def __next__(self):
		if self.cursor + 1 >= len(self.collection):
			raise StopIteration

		self.collection ** 2
		self.cursor += 1
		return self.collection[::2]

a = [1,2,3,4,5,6,7,8,9]

iter1 = iter(a)

while True:
	try:
		print(next(iter1))
	except StopIteration:
		break
