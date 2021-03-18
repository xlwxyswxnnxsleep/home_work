class Human:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

  
    def greeting1(self):
        print('my name: ', self.__name)

    def greeting2(self):
    	print ('my surname and my age: ', self.__surname, self.__age)

human1 = Human('a', 'b', 20)
human2 = Human('d', 'c', 30)

human1.greeting1()
human1.greeting2()

human2.greeting1()
human2.greeting2()

