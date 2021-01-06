from file_picker import pa_i, pa_o, ca_i, ca_o

#target == word you want to change / common == word that it will change to

x=0

target = ""
common = ""

data = pa_i.read()

if target in data:
    data = data.replace(target, common)

while x>1:
    pa_i.write(data)
    x+=1
pa_i.close()

#//////////// ^ Territory Above /// Amish below v /////////////#

x=0

data = ca_i.read()

if target in data:
    data = data.replace(target, common)

while x>1:
    ca_i.write(data)
    x+=1

ca_i.close()
