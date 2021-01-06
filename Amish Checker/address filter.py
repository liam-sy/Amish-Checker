import csv

from file_picker import pa_i, pa_o, ca_i, ca_o

def filter_address(file_i, file_o):
    raw_list = []
    x = 0

    file_o.seek(0)
    file_o.truncate()

    #Take out only the "Address" column and copy it line by line into the output document
    raw_data = csv.DictReader(file_i)
    for row in raw_data:
        raw_list.append(row['Street Address'])
    file_i.close()
    file_o.write("Address\n")
    for row in raw_list:
        raw_list_string = str(raw_list[x])
        file_o.write(str(raw_list_string)+"\n")
        x += 1

filter_address(pa_i, pa_o)
pa_i.close()
pa_o.close()

filter_address(ca_i, ca_o)
ca_i.close()
ca_o.close()