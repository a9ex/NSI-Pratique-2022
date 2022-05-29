def maxliste(liste):
    max = liste[0]
    for i in liste:
        if i > max:
            max = i
    return max