# Program Kalkulator Sederhana

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

def menu():
    print("=== Kalkulator Sederhana ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")
    pilihan = input("Masukkan pilihan Anda (1-5): ")
    return pilihan

def main():
    while True:
        pilihan = menu()

        if pilihan == "5":
            print("Terima kasih telah menggunakan kalkulator ini.")
            break

        if pilihan in ["1", "2", "3", "4"]:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
        
            if pilihan == "1":
                print(f"Hasil: {tambah(a, b)}")
            elif pilihan == "2":
                print(f"Hasil: {kurang(a, b)}")
            elif pilihan == "3":
                print(f"Hasil: {kali(a, b)}")
            elif pilihan == "4":
                if b != 0:
                    print(f"Hasil: {bagi(a, b)}")
                else:
                    print("Kesalahan: Pembagian dengan nol tidak diperbolehkan.")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama
main()
