
#recherche
def chercher(x,T):
    if x in T :
        return T.index(x)
    return -1

#moyenne
moyenneT = lambda T: sum(T)/ len(T)

#minimum d'un tableau
def minTableau(T):
    min = T[0]
    for i in range(len(T)):
        if min > T[i]:
            min = T[i]
    
    return min

#somme de deux vecteurs
def somme_deux_vecteurs(X,T):
    y,somme,Taille = [],0,len(X) == len(T)

    if not Taille:
        return "pas possible"

    for i in range(len(X)):
        somme = T[i] + X[i]
        y.append(somme)
    return y

#occurence
occurence = lambda n,T: T.count(n)

#tri
tri = lambda T: sorted(T)

#Grand
def grands(L,x):
    count = 0 
    for i in range(len(L)):
        if x < L[i]:
            count+=1
    return count

#petit
def petit(L,x):
    count = 0 
    for i in range(len(L)):
        if x > L[i]:
            count+=1
    return count


def supprimer(T,x):
    for t in T:
        if t == x:
            print(T)
            T.remove(t)
            
    
    return T

def AfficherSousSequence(T):
    L = [T[0]]
    z = []
    for i in range(len(T)-1):
        if T[i+1] >= T[i]:
            L.append(T[i+1])
        else:
            z.append(L)
            L = [T[i+1]]
    return z
  

       


def total_vente(ventes):
    somme = 0 
    for vente in ventes:
        somme += ventes[vente]
    return somme

def max_vente(ventes):
    m = max(ventes.values())
    for vente in ventes:
        if ventes[vente] == max:
            return vente


def Intersersection(t1,t2):
    return list(set(t1) & set(t2))


        
# ----------Python OOP -------------------------
class compte:
    def __init__(self, soldeInitial, nomclient, numCompteClient, adresseClient):
        self.__solde = soldeInitial
        self.__nom = nomclient
        self.numCompte = numCompteClient
        self.adresse = adresseClient
    
    def affiche(self):
        print(
        f"""
            {self.__nom} qui habite a {self.adresse}
            a {self.__solde}MAD dans le compte {self.numCompte}
        """
        )
    
    # __mul__ __sub__
    def __add__(self,somme):
        if type(somme) in (int, float):
            self.__solde-= somme
    
    def __str__(self):
       return "Transformed in string"


# ---------- Tkinter -------------------

from tkinter import *

window = Tk()
window.geometry('600x400')
window.title("Pharmacie")

hello = Label(window, text="PHARMACIE", fg="purple")
hello.pack()

champ = Entry(window)
champ.pack()

window.mainloop()
