def rechercheMinMax(tab):
    mini = None
    max = None
    for nbr in tab:
        if mini is None or nbr < mini:
            mini = nbr
        if max is None or nbr > max:
            max = nbr
    return {'mini': mini, 'max': max}