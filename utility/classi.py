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

class Triangolo:
    def __init__(self, a,b,c):
        self.cateto1 = a
        self.cateto2 = b 
        self.cateto3 = c
    def perimetro(self):    
        '''calcola il perimetro del triangolo'''
        perimetro = self.cateto1+self.cateto2+self.cateto3
        return perimetro
    def area(self):
        '''calcola area del triangolo'''
        if self.cateto1<(self.cateto2+self.cateto3) and self.cateto2<(self.cateto1+self.cateto3) and self.cateto3<(self.cateto1+self.cateto2):
            p=self.perimetro()
            area=math.sqrt(p*(p-self.cateto1)*(p-self.cateto2)*(p-self.cateto3))
            print("l'area del triangolo è "+str(area))
            return area
        else:
            print("i segmenti inseriti non formano un triangolo")

        
