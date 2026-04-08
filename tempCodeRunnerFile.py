
def signeGagnant(signeIa, signeJoeur):
    res = ""
    if signeIa == signeJoeur :
        res = "null"
    elif signeIa == "pierre" and signeJoeur == "ciseaux" or signeIa == "feuille" and signeJoeur == "pierre"  or signeIa == "ciseaux" and signeJoeur =="feuille":
        res = "ia à gagné"
    elif signeIa == "ciseaux" and signeJoeur == "pierre" or signeIa == "pierre" and signeJoeur == "feuille"  or signeIa == "feuille" and signeJoeur =="ciseaux":
        res= "joueur à gagné"
    return res


print (signeGagnant('pierre', 'ciseaux'))
print (signeGagnant('feuille', 'pierre'))
print (signeGagnant('ciseaux', 'feuille'))

print (signeGagnant("ciseaux", "ciseaux"))
print (signeGagnant('pierre','pierre'))
print (signeGagnant('feuille', 'feuille'))

print (signeGagnant('feuille', 'pierre'))
print (signeGagnant('pierre', 'ciseaux'))
print (signeGagnant('ciseaux', 'feuille'))
