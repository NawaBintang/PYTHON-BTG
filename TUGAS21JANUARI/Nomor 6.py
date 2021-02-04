#Nawa Bintang Jagad Raya / 27 / XI 5

def Bebek(bebek, bagi):
    hasil_bagi = int(bebek / bagi)
    sisa = bebek % bagi
    return(hasil_bagi, sisa)

while True:
    a = int(input("Masukkan jumlah bebek: "))
    b = int(input("Masukkan jumlah teman: "))

    x, y = Bebek(a,b)
    print("Masing-masing", x)
    print("Bersisa: ", y)