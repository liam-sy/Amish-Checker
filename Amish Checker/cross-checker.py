import csv

a_list=[]
na_list=[]
x=0

#open and read the confirmed amish list
c_amish=open("files/new confirmed amish.csv", "r")
data1=c_amish.read()

#open and read the potential amish list
p_amish=open("files/new smicksburg.csv", "r")
data2=p_amish.readlines()

for i in range(len(data2)):
    target=data2[x].replace('\n', '')
    x+=1
    if target != "Address":
        if data1.find(str(target)) != -1:
            a_list.append(str(x)+") "+target)
        else:
            na_list.append(str(x)+") "+target)

print("\nConfirmed Amish\n")

for x in range(len(a_list)):
    print(str(a_list[x]))
    x+=1

print("\nNon-confirmed\n")

for x in range(len(na_list)):
    print(str(na_list[x]))
    x+=1

c_amish.close
p_amish.close