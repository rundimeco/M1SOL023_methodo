import re

def lire_fichier(chemin_fichier):
  f = open(chemin_fichier, "r")
  texteComplet = f.read()     
  f.close()    
  return texteComplet 

def trier_dic(dic):
  L = [[effectif,car] for car,effectif in dic.items()]
  L_sorted = sorted(L, reverse=True)
  return [[car,effectif] for effectif,car in L_sorted]

def moyenne(liste):
  total = 0
  for elem in liste:
    total+=elem
  return total/len(liste)

for chemin_fichier in 
chemin_fichier = "TD3_textes/Hugo.txt" #chemin vers Hugo.txt
texte = lire_fichier(chemin_fichier)
texte = re.sub("\n"," ", texte)
texte_sans_ponct = re.sub(",", "", texte)
texte_sans_ponct = re.sub(",|;|\.|'|\(|\)|-|\!|\?|:", " ", texte)

texte_sans_ponct_minuscules = texte_sans_ponct.lower()
liste_mots = texte_sans_ponct_minuscules.split()

dic= {}
for mot in liste_mots:
  if mot not in dic:
    dic[mot]=1
  else:
    dic[mot]+=1
print("-"*10)
print("Avant filtrage")
print("-"*10)
liste_triee = trier_dic(dic)
for mot, effectif in liste_triee[:10]:
  print(mot, effectif)

liste_mots_vides = ["la", "le", "ce", "à", "l", "et", "de", "que", "qui", "dans", "qu", "d", "en", "ne", "pas", "les", "un","n", "a","ou","où","du","des", "m","tout", "sur","mon"]
for mot_vide in liste_mots_vides:
  del dic[mot_vide]


print("-"*10)
print("Après filtrage")
print("-"*10)
liste_triee = trier_dic(dic)
for mot, effectif in liste_triee[:10]:
  print(mot, effectif)

print("-"*10)
print("Statistiques sur la longueur (occurrences)")
print("-"*10)
liste_longueurs = []
long_max= 0
mot_max = ""
long_min= 100
mot_min = ""
for mot in liste_mots:
  longueur = len(mot)
  liste_longueurs.append(longueur)
  if longueur>long_max:
    long_max = longueur
    mot_max = mot
  if longueur<long_min:
    long_min = longueur
    mot_min = mot
print("Longueur moyenne :", moyenne(liste_longueurs))
print("Mot le plus long : %s (%i)"%(mot_max,long_max))
print("Mot le plus court : %s (%i)"%(mot_min,long_min))

##Statistiques sur les formes

print("-"*10)
print("Statistiques sur la longueur (formes)")
print("-"*10)
liste_formes = set(liste_mots)
liste_longueurs = []
for mot in liste_formes:
  longueur = len(mot)
  liste_longueurs.append(longueur)
print("Longueur moyenne :", moyenne(liste_longueurs))

print("*"*10)
print("Statistiques sur les phrases")
print("*"*10)
liste_phrases = re.split("\.|\?|\!", texte)
liste_phrases = [x for x in liste_phrases if len(x)>0]
nb_aff = len(re.findall("\.", texte))
nb_int = len(re.findall("\?", texte))
nb_exc = len(re.findall("\!", texte))
print("Nombre de phrases :", len(liste_phrases))
print(" dont affirmatives :", nb_aff)
print(" dont interrogatives :", nb_int)
print(" dont exclamatives :", nb_exc)
#Remarquez le paradoxe
print("-"*10)
print("Statistiques sur la longueur des phrases")
print("-"*10)
liste_longueurs = []
long_max= 0
long_min= 1000
for mot in liste_phrases:
  longueur = len(mot)
  liste_longueurs.append(longueur)
  if longueur>long_max:
    long_max = longueur
  if longueur<long_min:
    long_min = longueur
print("Longueur moyenne :", moyenne(liste_longueurs))
print("Longueur minimum :", long_min)
print("Longueur maximum :", long_max)
