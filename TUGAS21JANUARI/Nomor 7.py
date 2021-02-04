#Nawa Bintang Jagad Raya / 27 / XI 5

num1 = int(input("Masukkan Panjang Segitiga: "))
num2 = int(input("Masukkan Tinggi Segitiga: "))

def luassegitiga(x,y):
    luas = float(x * y / 2)
    print(format(luas, ".2f"))

luassegitiga(num1,num2)