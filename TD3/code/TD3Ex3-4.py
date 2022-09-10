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

def get_moyenne(liste):
  total = 0
  for elem in liste:
    total+=elem
  return round(total/len(liste), 4)

def trier_dic(dic):
  L = [[effectif,car] for car,effectif in dic.items()]
  L_sorted = sorted(L, reverse=True)
  return [[car,effectif] for effectif,car in L_sorted]

def stats_caracteres(texte):
  dico_caracteres = {} 
  for caractere in texte:
    if caractere not in dico_caracteres:
      dico_caracteres[caractere]=1
    else: #On l'a vu une fois de plus :
      dico_caracteres[caractere]+=1
  c_trie=trier_dic(dico_caracteres)
  return c_trie

def stats_mots(texte):
  liste_mots = texte.split()
  dic= {}
  for mot in liste_mots:
    if mot not in dic:
      dic[mot]=1
    else:
      dic[mot]+=1
  return dic, liste_mots

def get_liste_mots_vides():
  L= ["la", "le", "ce", "à", "l", "et", "de", "que", "qui", "dans", "qu", "d", "en", "ne", "pas", "les", "un","n", "a","ou","où","du","des", "m","tout", "sur","mon"]
  return L
  
def stats_longueur(liste):
  liste_longueurs = []
  mot_max = ""
  mot_min = ""
  len_max = 0
  len_min = 100
  for mot in liste:
    liste_longueurs.append(len(mot))
    longueur = len(mot)
    if len(mot)>len_max:
      mot_max = mot 
      len_max = len(mot)
    elif len(mot)<len_min:
      mot_min = mot
      len_min = len(mot)
  return mot_min, mot_max, get_moyenne(liste_longueurs)

def stats_phrases(texte):
  liste_phrases = re.split("\.|\?|\!", texte)
  liste_phrases = [x for x in liste_phrases if len(x)>0]
  nb_aff = len(re.findall("\.", texte))
  nb_int = len(re.findall("\?", texte))
  nb_exc = len(re.findall("\!", texte))
  return liste_phrases, nb_aff, nb_int, nb_exc


##MAIN

liste_textes = ["TD3_textes/Hugo.txt", "TD3_textes/LExpress.txt"]
carte_identites_textes = []#pour stocker les statistiques ur tous les textes

for chemin_fichier in liste_textes:
  carte_identite = ["Texte :"+chemin_fichier]#pour chaque texte on stocke le nom
  ##Le texte sous différentes formes
  texte = lire_fichier(chemin_fichier)
  texte = re.sub("\n"," ", texte)
  texte_sans_ponct = re.sub(",|;|\.|'|\(|\)|-|\!|\?|:", " ", texte)

  ##STATISTIQUES SUR LES CARACTERES
  carte_identite.append("="*20)
  carte_identite.append("Caractères\n")#On ajoutera ainsi toutes les infos que l'on collecte

  liste_triee_car = stats_caracteres(texte) 
  cpt=1
  for caractere, effectif in liste_triee_car[:10]:
    frequence = round(effectif/len(texte), 6)
    s="%s. : --%s--(%s, %s)"%(cpt, caractere, effectif, frequence)
    carte_identite.append(s)
    cpt+=1

  ##STATISTIQUES SUR LES MOTS
  carte_identite.append("="*20)
  carte_identite.append("\nMots")

  texte_sans_ponct_minuscules = texte_sans_ponct.lower()
  dic_mots, liste_mots = stats_mots(texte_sans_ponct_minuscules)

  carte_identite.append("-"*20)
  carte_identite.append("Effectifs et Frequence Avant filtrage\n")

  liste_triee = trier_dic(dic_mots)
  nb_mots = len(liste_triee)
  cpt=1
  for mot, effectif in liste_triee[:5]:#modifier le 5 pour en voir plus
    frequence = round(effectif/nb_mots, 4)
    s = "%s. : %s (%s, %s)"%(cpt, mot, effectif, frequence)
    carte_identite.append(s)
    cpt+=1

  carte_identite.append("-"*20)
  carte_identite.append("Après filtrage\n")

  liste_mots_vides = get_liste_mots_vides()
  for mot_vide in liste_mots_vides:
    if mot_vide in dic_mots:
      del dic_mots[mot_vide]
  liste_triee = trier_dic(dic_mots)
  cpt=1
  for mot, effectif in liste_triee[:5]:#modifier le 5 pour en voir plus
    frequence = round(effectif/nb_mots, 4)
    s = "%s.: %s (%s, %s)"%(cpt, mot, effectif, frequence)
    carte_identite.append(s)
    cpt+=1

  carte_identite.append("-"*20)
  carte_identite.append("Statistiques sur la longueur (occurrences)\n")

  mot_min, mot_max, moyenne = stats_longueur(liste_mots)
  carte_identite.append("Longueur moyenne : %s"%moyenne)
  carte_identite.append("Mot le plus long : %s (%i)"%(mot_max,len(mot_max)))
  carte_identite.append("Mot le plus court : %s (%i)"%(mot_min,len(mot_min)))

  carte_identite.append("\n"+"-"*20)
  carte_identite.append("Statistiques sur la longueur (formes)\n")
  liste_formes = set(liste_mots)
  mot_min, mot_max, moyenne = stats_longueur(liste_formes)
  carte_identite.append("Longueur moyenne : %s" %moyenne)
  carte_identite.append("-"*20)

  ##STATISTIQUES SUR LES PHRASES
  carte_identite.append("="*20)
  carte_identite.append("Statistiques sur les phrases")
  carte_identite.append("-"*20)

  liste_phrases, nb_aff, nb_int,nb_exc = stats_phrases(texte)
  carte_identite.append("Nb phrases\t : %s"%len(liste_phrases))
  carte_identite.append("  affirm.\t : %s"%nb_aff)
  carte_identite.append("  interro.\t : %s"%nb_int)
  carte_identite.append("  exclam.\t : %s"%nb_exc)

  phr_min, phr_max, moyenne = stats_longueur(liste_phrases)
  carte_identite.append("Long moy\t : %s"%moyenne)
  carte_identite.append("Long min\t : %s"%len(phr_min))
  carte_identite.append("Long max\t : %s"%len(phr_max))
  carte_identite.append("-"*20)

  carte_identites_textes.append(carte_identite)
  

nb_stats = len(carte_identite)
nb_textes = len(liste_textes)

###Mise en forme des statistiques

for id_stat in range(nb_stats):#parcours des attributs (lignes)
  ligne = []
  for id_texte in range(nb_textes):#parcours des valeurs (colonnes)
    l = carte_identites_textes[id_texte][id_stat]
    if ":" in l:#nom d'attribut + valeur
      attribut, valeur = re.split(":", l)
      attribut = attribut+"\t"
      ligne.append(valeur)
    else:
      attribut = l
      break
      
  if "\n" in attribut:
    print(attribut)
  else:
    print(attribut+"<-->".join(ligne))
