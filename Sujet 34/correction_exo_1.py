alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o,','p','q','r','s','t','u','v','w','x','y','z']

def occurrence_max(chaine):
    occurence = [0]*26
    for char in chaine:
        if char in alphabet:
            occurence[alphabet.index(char)] += 1
    occ = 0
    pos = 0
    for i in range(len(occurence)):
        if occurence[i] > occ:
            occ = occurence[i]
            pos = i
    return alphabet[pos]

ch='je suis en terminale et je passe le bac et je souhaite poursuivre des etudes pour devenir expert en informatique'
print(occurrence_max(ch))
