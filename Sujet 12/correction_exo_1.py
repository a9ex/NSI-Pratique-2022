def moyenne(liste):
    somme = 0
    if len(liste) == 0:
        return "Erreur"
    for i in liste:
        somme += i
    return somme / len(liste)