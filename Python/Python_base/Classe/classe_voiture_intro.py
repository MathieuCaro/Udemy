# ===========================================================================
# Title: classe_voiture.py
# Description: This script enables to review the basics og Class methods
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================


# -----------------------------Import of modules-----------------------------


# ---------------------------------Functions----------------------------------
#Création de la classe Voiture
class Voiture:
    nb_voiture=0
    def __init__(self,marque):
        Voiture.nb_voiture+=1
        self.marque=marque

# ---------------------------------Main program-------------------------------
#Instance 1:
ma_voiture=Voiture("Audi") #création de l'instance 1
print(ma_voiture.marque)
print(Voiture.nb_voiture)

#Instance 2:
ta_voiture=Voiture("Peugeot") #création de l'instance 2
print(ta_voiture.marque)
print(Voiture.nb_voiture)