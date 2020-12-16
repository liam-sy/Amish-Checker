#target == word you want to change / common == word that it will change to

target=""
common=""

og_amish=open("files/Contact Filtered Export Contacts (4).csv", "r+")
data_a=og_amish.read()
og_amish.close()

og_smicksburg=open("files/Terr 089- (Smicksburg) - All Data Compiled.csv", "r+")
data_s=og_smicksburg.read()
og_smicksburg.close()

if target in data_a or data_s:
    data_a = data_a.replace(target, common)
    data_s = data_s.replace(target, common)

with open("files/Contact Filtered Export Contacts (4).csv", "w") as new_words_a:
    new_words_a.write(data_a)

with open("files/Terr 089- (Smicksburg) - All Data Compiled.csv", "w") as new_words_s:
    new_words_s.write(data_s)

new_words_a.close
new_words_s.close