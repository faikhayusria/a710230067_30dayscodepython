# Menggunakan loop for
for i in range(1, 6):
    print(f"Perulangan ke-{i}")

# Menggunakan loop while
count = 1
while count <= 5:
    print(f"Perulangan while ke-{count}")
    count += 1

FUNCTIONS

# Definisi fungsi
def hitung_luas_persegi(sisi):
    return sisi * sisi

# Menggunakan fungsi
sisi_persegi = 4
luas_persegi = hitung_luas_persegi(sisi_persegi)
print(f"Luas persegi dengan sisi {sisi_persegi} adalah {luas_persegi}")