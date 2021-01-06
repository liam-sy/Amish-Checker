from file_picker import pa_i, pa_o, ca_i, ca_o

#target == word you want to change / common == word that it will change to

target = ""
common = ""

def normalise(file):
    x=0
    data = file.read()

    file.seek(0)
    file.truncate()

    if target in data:
        data = data.replace(target, common)

    while x != 1:
        file.write(data)
        x += 1

    file.close()

    return file

normalise(pa_i)
pa_i.close

normalise(ca_i)
ca_i.close()