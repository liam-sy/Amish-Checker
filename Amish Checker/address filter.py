import csv

from file_picker import pa_i, pa_o, ca_i, ca_o

raw_list=[]
x=0

#Clear the output document
pa_o.truncate(0)

#Take out only the "Address" column and copy it line by line into the output document
raw_data=csv.DictReader(pa_i)
for row in raw_data:
    raw_list.append(row['Street Address'])
pa_i.close()
pa_o.write("Address\n")
for row in raw_list:
    raw_list_string=str(raw_list[x])
    pa_o.write(str(raw_list_string)+"\n")
    x+=1

pa_o.close()

#//////////// ^ Territory Above /// Amish below v /////////////#

raw_list=[]
x=0

#Clear the output document
ca_o.truncate(0)

#Take out only the "Address" column and copy it line by line into the output document
raw_data=csv.DictReader(ca_i)
for row in raw_data:
    raw_list.append(row['Address'])
ca_i.close()
ca_o.write("Address")
for row in raw_list:
    raw_list_string=str(raw_list[x])
    ca_o.write(str(raw_list_string)+"\n")
    x+=1

ca_o.close()

