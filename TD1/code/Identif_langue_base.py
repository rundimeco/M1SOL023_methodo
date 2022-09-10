import glob, sys, os
import re, json

def ouvrir(path):
  f = open(path, encoding="utf-8")
  ch = f.read()
  f.close()
  return ch

def get_models(chemin):
  dic = {}
  for path in glob.glob("%s/*/appr/*"%chemin):
#    toto, lg, titi, filename = re.split("\\\\", path)#mac/linux: re.split("/"...
    toto, lg, titi, filename = re.split("/", path)[-4:]
    dic.setdefault(lg, {})
    chaine = ouvrir(path)
    mots = chaine.split()
    for m in mots:
      dic[lg].setdefault(m, 0)
      dic[lg][m]+=1
  
  models = {}
  cpt = 0
  for lg, dic_mots in dic.items():
    L= []
    for mot, effectif in dic_mots.items():
      L.append([effectif, mot])
    toto = sorted(L, reverse=True)[:10]
    if cpt<3:
      ligne = [lg]
      for effectif, mot in toto:
        ligne.append("%s (%i)"%(mot, effectif))
      #cpt+=1
      print("\t&".join(ligne)+"\\\\")
    toto = [mot for effectif, mot in toto]    
    models[lg] = toto
  return models

import sys, os

if os.path.exists("models.json")==False:
  print("Processing %s"%sys.argv[1])
  models = get_models(sys.argv[1])
  w = open("models.json", "w", encoding = "utf-8")
  w.write(json.dumps(models))
  w.close()
else:
  print("Using models.json")

f = open("models.json")
dic_models = json.load(f)
f.close()

diagnostics = []
for path in glob.glob("%s/*/test/*"%sys.argv[1]):
  dic_mots = {}
  toto, lg_text, titi, filename = re.split("/", path)[-4:]
  chaine = ouvrir(path)
  mots = chaine.split()
  for m in mots:
    dic_mots.setdefault(m, 0)
    dic_mots[m]+=1
  L= []
  for mot, effectif in dic_mots.items():
    L.append([effectif, mot])
  toto = sorted(L, reverse=True)[:10]
  toto = [mot for effectif, mot in toto]
  liste_predictions = []
  for lg_model, most_frequent in dic_models.items():
    taille_intersection = len(set(toto).intersection(set(most_frequent)))
    liste_predictions.append([taille_intersection, lg_model])
  diagnostics.append([lg_text, sorted(liste_predictions, reverse=True)])


# In[52]:

print("Erreurs de prédiction (langue suivi du podium des intersections):")
for lg_text, predictions in diagnostics:
    lg_pred = predictions[0][1]
    if lg_text!=lg_pred:
      ligne = [lg_text]
      for eff, lg in predictions[:3]:
        ligne.append("%s (%i)"%(lg, eff))
      print("\t&".join(ligne)+"\\\\")#+"\\\\\n")
      


# In[ ]:



