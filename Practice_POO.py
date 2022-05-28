
class Car():

    def __init__(self) -> None:
        self.__length = 250
        self.__width = 120
        self.__wheels = 4
        self.__run_Car = False


    def run(self, running) -> None:
        self.__run_Car = running

        if (self.__run_Car):
            check = self.__internal_check()

        if (self.__run_Car and check):

            return 'The vehicle is running'

        elif(self.__run_Car and check == False):

            return 'Something got wrong we can not run'

        else:
            return 'The vehicle is stopped'


    def status(self):
        print(f'The vehicle has  {self.__wheels} wheels. A length of  {self.__length} and a width of {self.__width} ')


    def __internal_check(self):
        print('Cheking...')

        self.gasoline = 'ok'
        self.oil = 'ok'
        self.doors = 'ok'

        if(self.gasoline == 'ok' and self.oil == 'ok' and self.doors == 'ok' ):
            
            return True

        else:

            return False





MyCar =  Car()

print (MyCar.run(True))

MyCar.status()



print('**************To be continue we will create a second object ***************')



MyCar2 =  Car()

print (MyCar2.run(False))

MyCar2.status()


