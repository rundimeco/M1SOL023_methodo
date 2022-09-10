#!/usr/bin/env python
# coding: utf-8
# %%
import xml.etree.ElementTree as ET
tree = ET.parse("DATA/Corpus_rapv2.xml")
root = tree.getroot()


# %%
print(root.tag)


# %%
liste_paroles = []
liste_titres  = []
liste_artistes= []
for child in root.iter("chanson"): #on fait le tour des elements corpus, descendants de root chanson
    liste_paroles.append(child.find("paroles").text) #on cherche le contenu de l'element parole
    liste_titres.append(child.get("titre"))
    liste_artistes.append(child.get("artiste"))
print("premier titre: ''%s' de %s" %(liste_titres[0], liste_artistes[0]))

print("--"*20)
print(liste_paroles[0][:80])
print("--"*20)

print("Artistes:",set(liste_artistes))


# %%
from sklearn.feature_extraction.text import CountVectorizer
V = CountVectorizer() #l'outil chargé de transformer les textes en "tableaux de mots"


# %%
#On vectorise le corpus des paroles :

X = V.fit_transform(liste_paroles)
liste_mots_index = V.get_feature_names()
print(liste_mots_index[:50]) #une partie du vocabulaire trouvé dans le corpus ci-dessus


# %%
# On regarde ce que ça donne pour le premier document
# Le deuxième chiffre c'est l'index, le troisième l'effectif :


# %%
print("Pour les 5 premiers textes, ça donne : ")
for i in range(5):
    print(liste_paroles[i][:100])
    print(X[i])


# %%
# On a bien le "X", il nous manque le "y" :

y = liste_artistes

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

print("Il y a %i exemples dans le 'training set' et %i dans le 'test set'"%(
X_train.shape[0], X_test.shape[0]))


# %%
from sklearn.linear_model import Perceptron

ppn = Perceptron(eta0=0.1, random_state=0)
ppn.fit(X_train, y_train)
y_pred = ppn.predict(X_test)

# On fait la somme de tous les cas où la valeur dans y_test est bien trouvée dans y_pred
print('Bonne classification: %d' % (y_test == y_pred).sum())
print('Erreurs: %d' % (y_test != y_pred).sum())


# %%
dic_resultats = {} # pour recenser les erreurs et les bonnnes prédictions
for artiste in liste_artistes:
    #Un dictionnaire pour compter les résultats (initialisé à 0)
    dic_resultats[artiste] = {"VraiPositif":0, "FauxPositif":0, "FauxNegatif":0}

dic_errors = {}
for i in range(len(y_test)):
    artiste_test = y_test[i]
    artiste_pred = y_pred[i]
    if artiste_test == artiste_pred:#vrai positif
        dic_resultats[artiste_test]["VraiPositif"] +=1 # On ajoute 1, syntaxe équivalente à :
        #dic_resultats[artiste_test]["VraiPositif"] = dic_resultats[paroles_test]["VraiPositif"]+1
    else:
        error = "%s -> %s"%(artiste_test, artiste_pred)
        dic_errors.setdefault(error, 0)
        dic_errors[error]+=1
        dic_resultats[artiste_test]["FauxNegatif"]+=1 # Il en manque un ici (FN)
            
        dic_resultats[artiste_pred]["FauxPositif"]+=1 # Il y en a un de trop là (FP)
            
for artiste, res in dic_resultats.items():
    print(artiste, res)#paroles, 
print(dic_errors)


# %%
from sklearn.metrics import accuracy_score
print ('Accuracy: %.2f' % accuracy_score(y_test, y_pred))
#40 bonnes prédictions et 20 erreurs ça fait bien 2/3 (0,66) de bonnes prédictions:


# %%




