def calcul(n):
    valeurs = []
    while n != 1 :
        valeurs.append(n)
        if n%2 == 0:
            n = n//2
        else :
            n = n*3+1
    valeurs.append(1)
    return valeurs