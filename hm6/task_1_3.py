def createGenerator():
	mylist = range(8)
	for i in mylist:
		yield i

mygenerator = createGenerator()

for i in mygenerator:
	print(i)


