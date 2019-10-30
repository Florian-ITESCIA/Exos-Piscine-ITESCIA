def palindrome(str) :
    return str == str[::-1]

mot = input("Le mot   ")
M = mot
P = palindrome(M)
if P == True:
    print("est un palindrome")
else:
    print("n'est pas un palindrome")