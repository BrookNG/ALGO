#Laidi Zakaria




#Q1
def tamiser(tab, n, i):
    plus_grand = i
    gauche = 2 * i + 1
    droite = 2 * i + 2

    if gauche < n and tab[gauche] > tab[plus_grand]:
        plus_grand = gauche
    if droite < n and tab[droite] > tab[plus_grand]:
        plus_grand = droite

    if plus_grand != i:
        tab[i], tab[plus_grand] = tab[plus_grand], tab[i]
        tamiser(tab, n, plus_grand)


def construire_tas(tab):
    n = len(tab)
    for i in range(n // 2 - 1, -1, -1):
        tamiser(tab, n, i)
    return tab


vecteur = [10, 22, 5, 18, 20, 25, 40, 30, 35, 12]
tasmax = construire_tas(vecteur)
print(tasmax)


#Q2
def triTas(tab):
    n = len(tab)
    for i in range(n // 2 - 1, -1, -1):
        tamiser(tab, n, i)

    for i in range(n - 1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        tamiser(tab, i, 0)

    return tab[::-1]  


vecteur2 = [40, 35, 25, 30, 20, 10, 5, 22, 18, 12]
resultat = triTas(vecteur2)
print(resultat)

