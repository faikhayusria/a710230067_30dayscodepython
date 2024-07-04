class Karyawan:
    def __init__(self, nama, usia, gaji):
        self.nama = nama
        self.usia = usia
        self.gaji = gaji

    def tampilkan_informasi(self):
        print(f"Nama: {self.nama}")
        print(f"Usia: {self.usia}")
        print(f"Gaji: {self.gaji}")

    def naik_gaji(self, persen_kenaikan):
        self.gaji += self.gaji * persen_kenaikan / 100
        print(f"Gaji baru {self.nama} setelah kenaikan: {self.gaji}")

    def tambah_bonus(self, bonus):
        self.gaji += bonus
        print(f"Gaji baru {self.nama} setelah bonus: {self.gaji}")

class Manager(Karyawan):
    def __init__(self, nama, usia, gaji, departemen):
        super().__init__(nama, usia, gaji)
        self.departemen = departemen

    def tampilkan_informasi(self):
        super().tampilkan_informasi()
        print(f"Departemen: {self.departemen}")

    def ganti_departemen(self, departemen_baru):
        self.departemen = departemen_baru
        print(f"{self.nama} sekarang bertugas di departemen: {self.departemen}")

# Contoh penggunaan kelas Karyawan dan Manager
karyawan1 = Karyawan("Aldi", 30, 5000000)
karyawan1.tampilkan_informasi()
karyawan1.naik_gaji(10)
karyawan1.tambah_bonus(500000)

manager1 = Manager("Citra", 35, 7000000, "Keuangan")
manager1.tampilkan_informasi()
manager1.naik_gaji(15)
manager1.ganti_departemen("Pemasaran")
