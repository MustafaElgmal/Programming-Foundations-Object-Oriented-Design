# create class spaceship

class spaceship:
    def __init__(self):
        # instance varibles
        self.callSign = ""
        self.__shieldStrength = 100

    # methodes
    def fireMissle(self):
        return "Pew!"

    def reduceShield(self, num):
        self.shieldStrength -= num
