import csv

raw_list=[]
x=0

open("files/new smicksburg.csv", "w").close()

s1=open("files/Terr 089- (Smicksburg) - All Data Compiled.csv")
raw_data=csv.DictReader(s1)
for row in raw_data:
    raw_list.append(row['Street Address'])
with open("files/new smicksburg.csv", "a+") as s2:
    s2.write("Address\n")
    for row in raw_list:
        raw_list_string=str(raw_list[x])
        s2.write(str(raw_list_string)+"\n")
        x+=1

s1.close()
s2.close()

#//////////// ^ Smicksburg above /// Amish below v /////////////#

raw_list=[]
x=0

open("files/new confirmed amish.csv", "w").close()

a1=open("files/Contact Filtered Export Contacts (4).csv")
raw_data=csv.DictReader(a1)
for row in raw_data:
    raw_list.append(row['Address'])
with open("files/new confirmed amish.csv", "a+") as a2:
    a2.write("Address")
    for row in raw_list:
        raw_list_string=str(raw_list[x])
        a2.write((str(raw_list_string)+" \n"))
        x+=1

a1.close()
a2.close()