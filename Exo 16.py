def distance_hamming(str1,str2) : # On initialise la fonction
    j = 0 # on initialise j qui sera le compteur de différence entre nos 2 mots
    if len(str1) == len(str2) : # on vérifie que les mots font la même taille
        for i in range(0,len(str1)) : # on parcours nos chaînes
            if str1[i] != str2[i] : # si le caractère en position i est différent entre mes 2 chaînes...
                j = j + 1 # alors j'ajoute 1 à mon compteur de différence
        print("La distance de Hamming entre " + str1 + " et " + str2 + " vaut " + str(j)) # j'affiche sous forme d'une phrase
    else :
        print("Les mots doivent être de la même taille !") # si les mots ne sont pas de la même taille, j'arrête mon programme et je signale à l'utilisateur.

str1 = input("Entrez le premier mot : ") # je demande à l'utilisateur de saisir un premier mot
str2 = input("Entrez le second mot : ") # puis un second mot
distance_hamming(str1,str2) # et j'exécute ma fonction.
