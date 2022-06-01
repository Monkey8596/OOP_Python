
class vehicles():
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model
        self.run_car = False
        self.fast = False
        self.brake = False

    def run(self):

        self.run_car = True

    def speed_up(self):

        self.fast = True

    def braking(self):
        
        self.brake = True

    def status(self):

        print(f'Make: {self.make} \nModel: {self.model} \nRunning: {self.run_car} \nSpeed up:  {self.fast} \nBrake:  {self.brake} ')




class Furgoneta(vehicles):

    def carga(self, pick):
        self.cargado = pick
        if(self.cargado):
            return 'The Furgoneta is full'
        else:
            return 'The Furgonota is not yet ready'




class Bike(vehicles):

    h_horse = ''

    def horse(self):
        self.h_horse = 'Horse with the bike'

    def status(self):

        print(f'Make: {self.make} \nModel: {self.model} \nRunning: {self.run_car} \nSpeed up:  {self.fast} \nBrake:  {self.brake} \n{self.h_horse} ')





class V_Electric(vehicles):
    def __init__(self, make, model):
        super(). __init__(make, model)

        self.autonomy = 100

    def charge(self):

        self.charging = True




MyBike = Bike('Honda', 'CBR')

MyBike.horse()

MyBike.status()


print('**************************')


MyFurgoneta = Furgoneta('Renault', 'Kangoo')

MyFurgoneta.run()

MyFurgoneta.status()

print (MyFurgoneta.carga(True))




class Electric_bike(V_Electric,vehicles ):
    pass


MyBike = Electric_bike('Orbea', 'HJT')

