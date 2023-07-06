def kompresi(data):
    hasilkompresi = ""
    hurufsebelumnya = ""
    x = 1
    if not data:
        return ""
    for char in data:
        if char != hurufsebelumnya:
            if hurufsebelumnya:
                hasilkompresi += str(x) + hurufsebelumnya
            x = 1
            hurufsebelumnya = char
        else:
            x += 1
    hasilkompresi += str(x)+hurufsebelumnya
    return hasilkompresi


def dekompresi(data):
    hasildekompresi = ""
    x = ""
    for char in data:
        if char.isdigit():
            x += char
        else:
            hasildekompresi += char*int(x)
            x = ""
    return hasildekompresi


file = open("file_kompress.txt", "r")
kalimat = file.read()
print("Kalimat: ", kalimat)
print("Masukkan Pilihan:")
print("1. Kompressi")
print("2. Dekompressi")
pilihan = input("pilihan 1/2:")

if pilihan == "1":
    hasilnya = kompresi(kalimat)
    print("Hasil Komperssi:", hasilnya)
else:
    hasilnya = dekompresi(kalimat)
    print("Hasil Kompressi:", hasilnya)
file.close()
filekompress = open("file_kompress1.txt", "w")
filekompress.write(hasilnya)