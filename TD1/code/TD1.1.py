
phr = input("Veuillez entrer une phrase : ")
print(phr)
cch = input("Entrez la lettre qu'il faut compter : ")
print(cch)
nc = i = 0
while i < len(phr):
  if phr[i] == cch:
    nc = nc + 1
  i = i + 1
print("La phrase contient", nc, " la lettre ", cch)
