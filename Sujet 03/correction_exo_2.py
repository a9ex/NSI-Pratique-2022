class Noeud: 
    ''' 
    Classe implémentant un noeud d'arbre binaire disposant de 3      
attributs : 
    - gauche : le sous-arbre gauche. 
    - valeur : la valeur de l'étiquette, 
    - droit : le sous-arbre droit. 
    ''' 
    def __init__(self, g, v, d): 
        self.gauche = g 
        self.valeur = v 
        self.droit = d 
     
    def __str__(self): 
        return str(self.valeur) 
         
    def est_une_feuille(self): 
        '''Renvoie True si et seulement si le noeud est une feuille''' 
        return self.gauche is None and self.droit is None 
 
 
def expression_infixe(e): 
    s = ''
    if e.gauche is not None: 
        s = '(' + s + expression_infixe(e.gauche) 
    s = s + str(e.valeur) 
    if e.droit is not None: 
        s = s + expression_infixe(e.droit) + ')' 
    # if ... : # Le sujet semble être incorrect, le if n'est pas requis // Ou alors ils voulaient qu'on utilise est_une_feuille mais ce n'est pas requis.
    return s

e = Noeud(Noeud(Noeud(None, 3, None), '*', Noeud(Noeud(None, 8, None), 
'+', Noeud(None, 7, None))), '-', Noeud(Noeud(None, 2, None), '+', 
Noeud(None, 1, None)))

print(expression_infixe(e))