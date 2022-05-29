def recherche(elt, tab):
    indice = -1
    for i in range(len(tab)):
        if tab[i] == elt:
            indice = i
    return indice