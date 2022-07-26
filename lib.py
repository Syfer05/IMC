
def calcul_imc():
    poids = int(input ("Quel est votre poids en kg\n"))
    taille = (int(input("Quelle est votre taille en cm\n")))/100
    resultat = poids / (taille**2)
    print("Votre IMC est de :", resultat, "\n\n")


def conseil():
        poids = int(input("Quel est votre poids en kg\n"))
        taille = (int(input("Quelle est votre taille en cm\n"))) / 100
        resultat = poids / (taille ** 2)
        if resultat >= 25:
            print("Perdez du poids svp!")
        elif resultat <18:
            print("Votre corps est en limite de fonctionnement")
        else:
            print("Continuer comme cela!")
