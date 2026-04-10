import random
import time

""""
heure = time.localtime();
indic = time.strftime ("%H:%M:%S",heure)
print ("x",indic)
"""

res = random.randint(0,100)
def regles():
    print("\n" + "=" * 40)
    print("JEU DU JUSTE PRIX ")
    print("=" * 40)
    print("🔹 Le but : trouver le nombre mystère")
    print("🔹 Le nombre est entre 0 et 100")
    print("🔹 À chaque essai :")
    print("   → 'C'est plus' = le nombre est plus grand")
    print("   → 'C'est moins' = le nombre est plus petit")
    print("🔹 Tu gagnes quand tu trouves le bon nombre")
    print("=" * 40 + "\n")




def choixNiveau () :
    print("\n" + "=" * 40)
    print ('Icic vous allez choisir le niveau de dificultes :')
    print ("=" *40)
    print ('Niveau 1 chiffre à trouvé entre 0 et 100')
    print ("Niveau 2 chiffre à trouvé entre 1 et 1000")
    print ("Niveau 3 chiffre à trouve entre 1 et 10000")
    while True: 
        try :
            res = int(input("Veuillez taper : 1,2 ou 3 pour choisir votre niveau : ")) 
            if res in [1,2,3] :
                return res
            else:
                print ("choix invalide ")
        except:
            print("Veuillez entre sous forme de Chiffre : 1,2 ou 3 pour selectionner le niveau : ")
        
    



def prix (niveau):
    print (niveau)
    res = random.randint(0,100)
    if niveau == 1 :
        res = random.randint(0,100)

    elif niveau == 2 :
        res = random.randint(0,10000)
   
    elif niveau == 3 :
        res = random.randint(0,10000)
    return res



def choixJoueur ():
    res = int (input(" Entre votre prix : "))
    return res

def final (prixJoueur, prixAlea):

        distance = abs(prixJoueur - prixAlea)
        if prixJoueur == prixAlea:
            return ("gagné")
            
        elif distance > prixAlea / 2:
            return ("tu refroidis")
        elif distance > prixAlea / 4:
            return ("tiède")
        else:
            return("très chaud")


"""   
    if prixJoueur == prixAlea :
        return ("C'est Gagné")
    elif prixJoueur < prixAlea :
        return ( "C'est plus")
    elif prixJoueur > prixAlea :
        return ("C'est moins") 
    else:
        return ("erreur")
"""


def boucle():
    debut = time.time() # import du temps a partir d'un temp déja défini 

    
    compteurEssai = 0
    p = prix(choixNiveau())     
    print (p)
    while True:

        temps_ecoule = time.time() - debut # ici on soustrait le temps actuels a celui du debut 
        if temps_ecoule >= 60: # si c'est sup a 60 on arrette mais 
            # le temps est calculé qu'entre chaque réponse
            print(" Temps écoulé : échec")
            break
        

        # joueur = choixJoueur()
        res = final(choixJoueur(), p)
        compteurEssai += 1
        print (res)
        if res == "gagné":
            break
    return compteurEssai
       


while True:
    essais = boucle()
    print("Essais :", essais)

    rejouer = input("Rejouer ? (o/n) : ")
    if rejouer != "o":
        break



