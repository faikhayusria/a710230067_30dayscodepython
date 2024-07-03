class Manager(Karyawan):
    def __init__(self, nama, usia, gaji, departemen):
        super().__init__(nama, usia, gaji)
        self.departemen = departemen

    def tampilkan_informasi(self):
        super().tampilkan_informasi()
        print(f"Departemen: {self.departemen}")

# Contoh penggunaan kelas Manager
manager1 = Manager("Citra", 35, 7000000, "Keuangan")

manager1.tampilkan_informasi()
manager1.naik_gaji(15)
