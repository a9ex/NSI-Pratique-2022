def inverse_chaine(chaine): 
    result = ''
    for caractere in chaine: 
       result = caractere + result
    return result 
 
def est_palindrome(chaine): 
    inverse = inverse_chaine(chaine) 
    return chaine == inverse
     
def est_nbre_palindrome(nbre): 
    chaine = str(nbre)
    return est_palindrome(chaine)

print(inverse_chaine('bac'))
print(est_palindrome('NSI'))
print(est_palindrome('ISN-NSI'))
print(est_nbre_palindrome(214312))
print(est_nbre_palindrome(213312))