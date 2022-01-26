

class spaceShip:

    def __init__(self):

        self.callSign = ""
        self.__shieldStrength = 100

    # constractor overloading

    def __init__(self, name):
        self.callSign = name
        self.__shieldStrength = 100

    def fireMissle(self):
        return "Pew!"

    def reduceShield(self, num):
        self.shieldStrength -= num
