# Program Menghitung Nilai Faktorial

def hitung_faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        faktorial = 1
        for i in range(1, n + 1):
            faktorial *= i
        return faktorial

def main():
    angka = int(input("Masukkan angka: "))
    hasil = hitung_faktorial(angka)
    print(f"Faktorial dari {angka} adalah {hasil}")

# Menjalankan program utama
main()
