# Function dan Validasi Data

def rata_rata(nilai):
    if len(nilai) == 0:
        return  "Data kosong"
    else:
        total = 0
        for n in nilai :
            total += n
        return total / len(nilai)

nilai_mahasiswa = [80, 75, 90, 60, 85]
hasil = rata_rata(nilai_mahasiswa)

print("Rata-rata:", hasil)