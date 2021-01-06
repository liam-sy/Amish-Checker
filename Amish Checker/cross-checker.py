import csv

from file_picker import pa_i, pa_o, ca_i, ca_o

a_list = []
na_list = []
x = 0

#open and read the confirmed amish list
data1 = ca_o.read()

#open and read the potential amish list
data2 = pa_o.readlines() 

#Check each line of the potential amish output doc against the entire amish output doc for matches
for i in range(len(data2)):
    target = data2[x].replace('\n', '')
    x += 1
    if target != "Address":
        if data1.find(str(target)) != -1:
            a_list.append(str(x)+") " + target)
        else:
            na_list.append(str(x)+") " + target)

#Print the matches, then the non-matches
print("\nConfirmed Amish\n")

for x in range(len(a_list)):
    print(str(a_list[x]))
    x += 1

print("\nNon-confirmed\n")

for x in range(len(na_list)):
    print(str(na_list[x]))
    x += 1

ca_o.close
pa_o.close
