# Program Mengelola Nilai Mahasiswa dengan Python List

# Data awal minimal 5 nilai
nilai = [70, 80, 90, 75, 85]

# Function menampilkan nilai
def tampilkan_nilai(data):
    print("Daftar Nilai:")
    for n in data:
        print(n, end=" ")
    print("\n")

# Function tambah nilai
def tambah_nilai(data):
    tambah = int(input("Masukkan nilai baru: "))
    data.append(tambah)
    print("Nilai berhasil ditambahkan!\n")

# Function hapus nilai
def hapus_nilai(data):
    hapus = int(input("Masukkan nilai yang ingin dihapus: "))

    if hapus in data:
        data.remove(hapus)
        print("Nilai berhasil dihapus!\n")
    else:
        print("Nilai tidak ditemukan!\n")

# Function hitung rata-rata
def rata_rata(data):
    total = sum(data)
    rata = total / len(data)
    return rata

# Function nilai tertinggi dan terendah
def nilai_max_min(data):
    print("Nilai tertinggi :", max(data))
    print("Nilai terendah  :", min(data))

# Menu program
while True:
    print("===== MENU =====")
    print("1. Tampilkan Nilai")
    print("2. Tambah Nilai")
    print("3. Hapus Nilai")
    print("4. Hitung Rata-rata")
    print("5. Nilai Tertinggi & Terendah")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_nilai(nilai)

    elif pilihan == "2":
        tambah_nilai(nilai)

    elif pilihan == "3":
        hapus_nilai(nilai)

    elif pilihan == "4":
        print("Rata-rata nilai :", rata_rata(nilai))
        print()

    elif pilihan == "5":
        nilai_max_min(nilai)
        print()

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!\n")