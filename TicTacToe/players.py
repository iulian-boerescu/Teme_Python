class Player:

    def __init__(self):
        print("Please, type your name:")
        self._name = input('> ')
        self._sign = None
        self._wins = 0

    @property
    def name(self):
        return self._name

    @property
    def sign(self):
        return self._sign

    @sign.setter
    def sign(self, sign):
        self._sign = sign

    def __str__(self):
        return self._name
