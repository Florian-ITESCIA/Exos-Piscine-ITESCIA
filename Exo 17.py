mot = input("Le mot ")  # On demande à l'utilisateur de saisir le mot qu'il souhaite
if mot == mot[::-1]: # On parcours la chaîne que l'utilisateur a saisit et si la chaîne dans un sens est la même dans l'autre sens...
   print ("est un palindrome") # on affiche que le mot est un palindrome
else:
   print("n'est pas un palindrome") # sinon le mot n'en est pas un.
