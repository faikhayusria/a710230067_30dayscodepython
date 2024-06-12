# Definisi set
buah = {"apel", "jeruk", "mangga"}

# Menambahkan elemen ke dalam set
buah.add("pisang")

# Menghapus elemen dari set
buah.remove("jeruk")

# Menggabungkan dua set
buah_lain = {"anggur", "mangga", "kiwi"}
buah_gabungan = buah.union(buah_lain)

# Mencari irisan dari dua set
buah_irisan = buah.intersection(buah_lain)

print("Set setelah penambahan dan penghapusan:", buah)
print("Set gabungan:", buah_gabungan)
print("Set irisan:", buah_irisan)