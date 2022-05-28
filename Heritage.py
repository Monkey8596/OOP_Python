
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

        print(f' Make: {self.make} /n Model: {self.model} ')