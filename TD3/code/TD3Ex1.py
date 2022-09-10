def lire_fichier(chemin_fichier):
  f = open(chemin_fichier, "r")
  texteComplet = f.read()     
  f.close()    
  return texteComplet 

chemin_fichier = "TD3_textes/Hugo.txt" #chemin vers Hugo.txt
texte = lire_fichier(chemin_fichier)
dico_caracteres = {} 

for caractere in texte:
  if caractere not in dico_caracteres:#on crée une entrée
    dico_caracteres[caractere]=1
  else: #On l'a vu une fois de plus :
    dico_caracteres[caractere]+=1

def trier_dic(dic):
  L = [[effectif,car] for car,effectif in dic.items()]
  L_sorted = sorted(L, reverse=True)
  return [[car,effectif] for effectif,car in L_sorted]

c_trie=trier_dic(dico_caracteres)

for caractere, effectif in c_trie[:5]:
  print("--%s--(%s)"%(caractere, effectif))
