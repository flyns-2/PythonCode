import random 

choix = ["pierre", "feuille", "ciseaux"]# liste des signes a choisir



def  ordiChoix (): #fonction qui demande à l'ordi de choisi un signe parmis la liste signe
    return random.choice(choix)



def joueurChoix():
    print(choix)
    res = input("Entrer votre signe : ").strip().lower()
    print("r:", res)
    
    while res not in choix:
        print(choix)
        res = input('Choisissez un signe valide : ').strip().lower()
    
    return res


def signeGagnant(signeIa, signeJoeur):
    res = ""
    if signeIa == signeJoeur :
        return "egalite"
    elif signeIa == "pierre" and signeJoeur == "ciseaux" or signeIa == "feuille" and signeJoeur == "pierre"  or signeIa == "ciseaux" and signeJoeur =="feuille":
        return "ia"
    elif signeIa == "ciseaux" and signeJoeur == "pierre" or signeIa == "pierre" and signeJoeur == "feuille"  or signeIa == "feuille" and signeJoeur =="ciseaux":
        return 'joueur'
    return res



def compteur():
    compteurJoueur = 0
    compteurIA = 0

    while compteurJoueur < 3 and compteurIA < 3:
        joueur = joueurChoix()
        ia = ordiChoix()

        print("IA :", ia)

        gagnant = signeGagnant(ia, joueur)

        if gagnant == "joueur":
            compteurJoueur += 1
        elif gagnant == "ia":
            compteurIA += 1
        else:
            print("égalité")

        print("Score :",  "j",compteurJoueur, "-", compteurIA,"ia")
        print("------")

compteur()

"""     d
print (signeGagnant('pierre', 'ciseaux'))
print (signeGagnant('feuille', 'pierre'))
print (signeGagnant('ciseaux', 'feuille'))

print (signeGagnant("ciseaux", "ciseaux"))
print (signeGagnant('pierre','pierre'))
print (signeGagnant('feuille', 'feuille'))

print (signeGagnant('ciseaux', 'pierre'))
print (signeGagnant('pierre', 'ciseaux'))
print (signeGagnant('ciseaux', 'feuille'))


regles = { "pierre": "ciseaux", "ciseaux": "feuille", "feuille": "pierre" }

print(regles['pierre'] == "ciseaux")
"""


