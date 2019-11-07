def distance_hamming(str1,str2) :
    j = 0
    if len(str1) == len(str2) :
        for i in range(0,len(str1)) :
            if str1[i] != str2[i] :
                j = j + 1
        print("La distance de Hamming entre " + str1 + " et " + str2 + " vaut " + str(j))
    else :
        print("Les mots doivent être de la même taille !")

str1 = input("Entrez le premier mot : ")
str2 = input("Entrez le second mot : ")
distance_hamming(str1,str2)