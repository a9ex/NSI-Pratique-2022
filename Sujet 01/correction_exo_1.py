def recherche(catactere, mot):
    occurence = 0
    for c in mot:
        if c == catactere:
            occurence += 1
    return occurence