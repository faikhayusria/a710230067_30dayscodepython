# Definisi dictionary
data_mahasiswa = {
    "001": {"nama": "Alice", "umur": 20, "jurusan": "Informatika"},
    "002": {"nama": "Bob", "umur": 21, "jurusan": "Sistem Informasi"},
    "003": {"nama": "Charlie", "umur": 22, "jurusan": "Teknik Komputer"}}

# Mengakses data dari dictionary
id_mahasiswa = "002"
mahasiswa = data_mahasiswa.get(id_mahasiswa, "Tidak ditemukan")

print(f"Data mahasiswa dengan ID {id_mahasiswa}: {mahasiswa}")