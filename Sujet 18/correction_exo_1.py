t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7] 
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

def mini(releve, date):
    valeur_mini = releve[0]
    index = 0
    for i in range(len(releve)):
        if releve[i] < valeur_mini:
            valeur_mini = releve[i]
            index = i
    return valeur_mini, date[index]

print(mini(t_moy, annees))