class Lavadora:

    def __init__(self) -> None:
        pass

    def lavar(self, temperatura = 'caliente' ):
        self._llenar_tanque_agua(temperatura)
        self._añadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_agua(self,temperatura):
        print (f'LLenar el tanque de agua {temperatura} ')

    def _añadir_jabon(self):
        print('Añadiendo jabon')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando ropa')

if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()

    