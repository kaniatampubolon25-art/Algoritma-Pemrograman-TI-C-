print("Program Pembagian Sederhana")

try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    hasil = angka1 / angka2

except ValueError:
    print("Error: Input harus berupa angka")

except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan angka nol")

else:
    print("Hasil pembagian adalah:", hasil)

finally:
    print("Program selesai.")