class Vehicle:
    def __init__(self, jenis, merk, tahun_rilis):
        self.jenis = jenis
        self.merk = merk
        self.tahun_rilis = tahun_rilis
 
    def suara(self):
        print("BRUMM")

class Mobil(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis, harga):
        super().__init__(jenis, merk, tahun_rilis)
        self.__harga = harga
    def get_harga(self):
        return self.__harga
    def suara(self):
        print("BRUMM")

    
class Motor(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis, harga):
        super().__init__(jenis, merk, tahun_rilis)
        self.__harga = harga
    def get_harga(self):
        return self.__harga
    def set_harga(self, harga_baru):
        self.__harga = harga_baru
    def suara(self):
        print("BRUMM")


p1 = Vehicle("Sedan", "Toyota", 2007 )
p2 = Mobil("pickup", "suzuki", 2010, 12.000)
p3 = Motor("matic", "Honda", 2012, 15.000)

print(f"kendaraan 1{p1.merk} : {p1.suara()} ")
print(f"kendaraan 2{p2.merk} : {p2.suara()}  dengan {p2.get_harga()}")
print(f"kendaraan 3{p3.merk} : {p3.suara()}  dengan {p3.get_harga()}")




      


