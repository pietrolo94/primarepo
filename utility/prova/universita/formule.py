import math

def somma_due_numeri(a:float, b:float):
    '''questa funzione somma due numeri float 
    e restituisce il loro risultato sommato'''
    somma = a+b
    print(somma)
    return somma

def area_triangolo(a,b):
    '''questa funzione calcola area di un triangolo con base e altezza'''
    area = (a*b)/2
    print("l'area del triangolo è " + str(area))
    return area

def area_rettangolo(a,b):
    '''questa funzione calcola area di un rettangolo con base e altezza'''
    area = a*b
    print("l'area del rettangolo è " +str(area))
    return area

def area_quadrato(a):
    '''questa funzione calcola area di un quadrato'''
    area = a**2
    print("l'area del quadrato è " +str(area))
    return area

def quadrato_numero(a):
    '''questa funzione calcola il quadrato di un numero'''
    quadrato = a**2
    print('il quadrato di ' +str(a)+' è '+str(quadrato))
    return quadrato

def area_cerchio(r):
    '''questa funzione calcola l'area del cerchio'''
    pi=3.14
    area= pi*(r**2)
    print("l'area del cerchio è "+str(area))

def formula_di_erone(a,b,c):
    if a<(b+c) and b<(a+c) and c<(a+b):
        p=(a+b+c)/2
        area=math.sqrt(p*(p-a)*(p-b)*(p-c))
        print("l'area del triangolo è "+str(area))
        return area
    else:
        print("i segmenti inseriti non formano un triangolo")

def volume_superfice_cubo(a):
    '''calcola volume e superfice di un cubo'''
    volume = a**3
    superfice = 6*(a**2)
    print("il volume è " +str(volume) + " la superfice è "+str(superfice))
    return volume, superfice 

def volume_sfera(r):
    '''calcoca il volume e la superficie di una sfera'''
    volume = 4/3*(math.pi*(r**3))
    superficie = 4*math.pi*(r**2)
    print("il volume della sfera è "+str(volume)+ " la superfice della sfera è "+str(superficie))
    return volume , superficie

