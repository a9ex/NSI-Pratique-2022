def recherche(elt, tab):
    liste = []
    for i in range(len(tab)):
        if tab[i] == elt:
            liste.append(i)
    return liste

print(recherche(3, [3, 2, 1, 3, 2, 1]))
print(recherche(4, [1, 2, 3]))