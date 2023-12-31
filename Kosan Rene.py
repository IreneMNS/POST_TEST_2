#Membersihkan layar
import os
os.system('cls')

from prettytable import PrettyTable

#Tabel Kosan
kosan_table = PrettyTable()
kosan_table.field_names = ["id","tipe","harga","ketersediaan"]
# Daftar tipe kosan beserta harga per bulan
kosan_rene = [
    {"id":1,"tipe": "Luxury one", "harga": 1000000,"ketersediaan": 10},
    {"id":2,"tipe": "Single room","harga":800000,"ketersediaan": 8},
    {"id":3,"tipe": "Sharing room","harga":500000, "ketersediaan": 5},
    {"id":4,"tipe": "Medium one", "harga" :500000, "ketersediaan": 3},
]

# Fungsi untuk menambahkan data
def Create_table(tipe, harga,ketersediaan):
    id_terakhir = kosan_rene[-1]["id"] if kosan_rene else 0
    new_id = id_terakhir + 1
    kosan_rene.append({"id": new_id, "tipe": tipe, "harga": harga, "ketersediaan": ketersediaan})
    print(f"Data dengan ID {new_id} berhasil ditambahkan.")

# Fungsi untuk menampilkan tabel data
def Read_table():
    kosan_table.clear_rows()
    for row in kosan_rene:
        kosan_table.add_row([row["id"], row["tipe"], row["harga"], row["ketersediaan"]])
    print(kosan_table)

# Fungsi untuk mengupdate data berdasarkan ID
def update_table(id, tipe, harga):
    for row in kosan_rene:
        if row["id"] == id:
            row["tipe"] = tipe
            row["harga"] = harga
            print(f"Data dengan ID {id} berhasil diupdate.")
            return
    print(f"Data dengan ID {id} tidak ditemukan.")

# Fungsi untuk menghapus data berdasarkan ID
def Delete_table(id):
    for row in kosan_rene:
        if row["id"] == id:
            kosan_rene.remove(row)
            print(f"Data dengan ID {id} berhasil dihapus.")
            return
    print(f"Data dengan ID {id} tidak ditemukan.")

#Fungsi Untuk melakukan transaksi
def transaksi_pembelian():
    print("Data Kosan yang kosong: ")
    Read_table()
    pilihan_tipe = int(input('Pilih tipe kosan(ID):'))

    for data in kosan_rene:
        if data ["id"] == pilihan_tipe:
            tipe_kosan = data["tipe"]
            harga_per_bulan = data["harga"]
            break
    else:
        print('Tipe kosan tidak ada, mungkin anda keliru')
        return
    
    Nama_sewa = input('Masukkan nama anak kos: ')
    Rentang_waktu = int(input('Masukkan rentang waktu sewa kos: '))
    Total_harga = int(harga_per_bulan*Rentang_waktu)

    print("Detail Penyewaan")
    print(f"Nama penyewa{Nama_sewa}")
    print(f"Tipe Kosan{tipe_kosan}")
    print(f"Rentang waktu sewa {Rentang_waktu}")
    print(f"Total harga{Total_harga}")

# Program utama
if __name__ == "__main__":
    Password = "admini"

while True:
    Option = input('Anda masuk sebagai?(Admin/User):')

    if Option == 'Admin':
        Kode = input('Masukkan Kode Admin:')
        if Kode != Password : 
            print('wah ada yang salah')
            continue

        #Program Utama Admin
        while True:
            print("==========MENU ADMIN==========")
            print("          1. CREATE           ")
            print("          2. READ             ")
            print("          3. UPDATE           ")
            print("          4. DELETE           ")
            print("          5. EXIT             ")
            print("==============================")

            pilihan = input("Pilih tindakan (1/2/3/4/5): ")

            if pilihan == "1":
                id = int(input("Masukkan id: "))
                tipe = input("Masukkan Tipe Kosan: ")
                harga = int(input("Masukkan Harga per Bulan: "))
                ketersediaan = int(input('Masukkan sisa kosong: '))
                Create_table(tipe, harga,ketersediaan)
        
            elif pilihan == "2":
                Read_table()

            elif pilihan == "3":
                id = int(input("Masukkan ID yang akan diupdate: "))
                tipe = input("Masukkan Tipe Kosan baru: ")
                harga = int(input("Masukkan Harga per Bulan baru: "))
                ketersediaan = int(input('Masukkan sisa kosong: '))
                update_table(id, tipe, harga)

            elif pilihan == "4":
                id = int(input("Masukkan ID yang akan dihapus: "))
                Delete_table(id)

            elif pilihan == "5":
                break

            else:
                print("Pilihan tidak valid. Coba lagi.")
                

    elif Option == 'User':
        print("Selamat datang di program transaksi!")

    while True:
        print("--------------------------------")
        print("     1. Mulai Transaksi         ")
        print("     2. Keluar                  ")
        print("--------------------------------")
        Option_user = input("Pilih menu (1/2): ")

        if Option_user == "1":
            transaksi_pembelian()
        elif Option_user == "2":
            print("Terima kasih! Sampai jumpa.")

        else:
            print("Inputan yang anda masukkan salah")
        break





    
