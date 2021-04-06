class MyOpen():
        def __init__(self, file_name, method):
            self.file = open(file_name, method)
        def __enter__(self):
            return self.file
        def __exit__(self, type, value, traceback):
            self.file.close()

with MyOpen('file.txt', 'w') as f:
	print (f)
        	
