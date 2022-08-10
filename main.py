from lib import calcul_imc
from lib import conseil

#-Calcul de l'IMC!
#-Analyse du poids en fct de personnes demême caracteristiques (Comparaison moyenne sur BDD)
#-Annonce de régime selon le poids actuel (3 programmes 1 Je dois groissir, 2 dois maigrir, 3 change rien)
#-Gérer un historique des mesures sur le temps du client (pas forcément sur la BDD, le local peut-être suffisant au début)




def menu():
    choix = input("Veuillez choisir votre fonctionnalité!\n 1:Calcul IMC \n 2:Comparaison \n 3:Conseil \n 4:Historique \n q:Quitter \n")
    if choix == "1":
        calcul_imc()
    elif choix == "2":
        pass
    elif choix == "3":
        conseil()
    elif choix == "4":
        pass
    elif choix == "q":
        exit()
    menu()
#def calcul_imc():

menu()