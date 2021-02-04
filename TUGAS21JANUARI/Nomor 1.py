#Nawa Bintang Jagad Raya / 27 / XI 5

def penjumlahan( *vartuple ):
    print ("jumlah adalah: ")
    jumlah = 0
    for var in vartuple:
        jumlah = jumlah + var
    print(jumlah)

def rata(*vartuple):
    print("rata-ratanya adalah: ")
    rerata = 0
    tot = 0
    for var in vartuple:
        tot = tot + var
    rerata = tot / len(vartuple)
    print(rerata)
    # Empat argumen
penjumlahan( 10, 30, 50, 70 )
rata( 10, 30, 50, 70 )