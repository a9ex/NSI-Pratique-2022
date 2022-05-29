def RechercheMin(liste):
    min = liste[0]
    pos = 0
    for i in range(len(liste)):
        if liste[i] < min:
            min = liste[i]
            pos = i
    return pos
