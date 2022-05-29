def delta(liste):
    resultat = [liste[0]]
    for i in range(1, len(liste)):
        resultat.append(liste[i]-liste[i-1])
    return resultat