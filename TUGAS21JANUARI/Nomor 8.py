#Nawa Bintang Jagad Raya / 27 / XI 5

def Modus(listangka):
    count = 0
    terbanyak = listangka[0]

    for i in listangka:
        flag = listangka.count(i)
        if flag >= count:
            count = flag
            terbanyak = i
    return(terbanyak)

while True:
    a = input("Masukkan angka: ")

    list_angka = a.split()
    print("Modusnya adalah: ", Modus(list_angka))