import random

with open("mot.txt", "r", encoding="utf-8") as f:
    mots = [ligne.strip().lower() for ligne in f]

mot_a_deviner = random.choice(mots)


def lettreJoueur():
    while True:
        res = input('Entrer une lettre : ').lower()
        if len(res) == 1 and res.isalpha():
            return res
        print("Entrer une seule lettre valide.")

def lettreInMot (lettre) :
    return lettre in mot_a_deviner


def jouer ():
    vies  = 7 
    lettre_trouvees= ""
    while vies > 0:
        print("Mot :", " ".join([l if l in lettre_trouvees else "_" for l in mot_a_deviner])) # pour chaque l dans mot a deviné si l in lettre_ trouvee on l'affiche sinon on laisse _
        lettre = lettreJoueur()
        if lettre in lettre_trouvees :
            print ("lettre déja trouvé ")
            continue
        lettre_trouvees += lettre
        if all(l in lettre_trouvees for l in mot_a_deviner):
            print ("Vous avez trouvé le mot : ", mot_a_deviner)
            break
        elif lettre not in mot_a_deviner :
            vies -= 1 
            print ("lettre incorrectes il vous reste ", vies, " vies")
    if vies == 0:
        print ("vous avez perdu ! le mot était : ", mot_a_deviner)

jouer()
