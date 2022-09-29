strTxt = ""
dir = "TXTs\\resposta1.txt"
with open(dir) as f:
    strTxt = f.read()
print(strTxt.split("\n"))