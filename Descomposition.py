class Automobile:
    def __init__(self, model, make, color):
        self.model = model
        self.make = make
        self.color = color
        self._status = 'Rest'
        self._motor = Motor(Cylinders=4)

    def acelerar(self, type= 'despacio' ):
        if type == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._status = 'Movimiento'

    # def windows(self, up):
    #     if up == True:
    #         self.up = up
    #     else:
    #         self.up = 0


class Motor:
    def __init__(self, Cylinders, type= 'Gasoline' ):
        self.Cylinders = Cylinders
        self.type = type
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass
        
