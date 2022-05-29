def moyenne(liste):
    somme = 0
    coefficient = 0
    for note in liste:
        somme = somme + note[0]*note[1]
        coefficient = coefficient + note[1]
    return somme/coefficient
