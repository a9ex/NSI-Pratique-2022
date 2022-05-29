def renverse(mot):
    rev = ""
    for i in range(len(mot)-1, -1, -1):
        rev += mot[i]
    return rev