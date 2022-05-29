def recherche(tab):
    tableau = []
    for i in range (1, len(tab)):
        if tab[i-1]+1 == tab[i]:
            tableau.append((tab[i-1], tab[i]))
    return tableau


print(recherche([5, 1, 2, 3, 8, -5, -4, 7]))

