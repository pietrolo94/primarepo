import math
class Cubo:
    def __init__(self, a:float):
        self.lato = a
    def volume (self):
        '''calcola volume di un cubo'''
        volume = self.lato**3
        return volume
    def superficie(self):
        '''calcola la superficie di un cubo'''
        superficie = self.lato**2*6
        return superficie
    

class Sfera:
    def __init__(self, r:float):
        self.raggio = r
    def volume(self):
        '''calcola il volume di una sfera'''
        volume = 4/3*(math.pi*(self.raggio**3))
        return volume
    def superfice(self):
        '''calcola la superficie di una sfera'''
        superficie = 4*math.pi*(self.raggio**2)
        return superficie
