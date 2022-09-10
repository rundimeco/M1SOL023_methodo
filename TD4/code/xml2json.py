import xmltodict
import sys
import json

for fic in sys.argv[1:]:
  f = open(fic)
  s = f.read()
  f.close()
  dic = xmltodict.parse(s)

  w = open(f"{fic}.json", "w")
  w.write(json.dumps(dic, indent =2, ensure_ascii=False))
  w.close()
