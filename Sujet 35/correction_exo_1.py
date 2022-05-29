def moyenne(liste):
    somme = 0
    for i in liste:
        somme += i
    return somme / len(liste)

# Assertions à tester fournies dans le sujet
assert moyenne([1]) == 1
assert moyenne([1,2,3,4,5,6,7]) == 4
assert moyenne([1,2]) == 1.5