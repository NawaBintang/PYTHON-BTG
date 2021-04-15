class Atlet:
    '''Dasar kelas semua atlet'''
    jumlah_atlet = 0

    def __init__(self, nama, nomorpunggung):
        self.nama = nama
        self.nomorpunggung = nomorpunggung
        Atlet.jumlah_atlet += 1

    def tampilkan_jumlah(self):
        print("Total atlet:", Atlet.jumlah_atlet)
    
    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("Nomor Punggung:", self.nomorpunggung)

atlet1 = Atlet("Zlatan Ibrahimovic", 11)
atlet2 = Atlet("Erling Haaland", 9)
atlet3 = Atlet("Cristiano Ronaldo", 7)
atlet4 = Atlet("Lionel Messi", 10)

atlet1.tampilkan_profil ()
atlet2.tampilkan_profil ()
atlet3.tampilkan_profil ()
atlet4.tampilkan_profil ()
print("Total atlet :", Atlet.jumlah_atlet)