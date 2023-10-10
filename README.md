# POST_TEST_2
PENGUMPULAN FLOWCHART DAN CODING

    #Membersihkan layar
    <import os>
    <os.system('cls')>

    from prettytable import PrettyTable

    #Tabel Kosan
    kosan_table = PrettyTable()
    kosan_table.field_names = ["id","tipe","harga","ketersediaan"]
    #Daftar tipe kosan beserta harga per bulan
    kosan_rene = [
    {"id":1,"tipe": "Luxury one", "harga": 1000000,"ketersediaan": 10},
    {"id":2,"tipe": "Single room","harga":800000,"ketersediaan": 8},
    {"id":3,"tipe": "Sharing room","harga":500000, "ketersediaan": 5},
    {"id":4,"tipe": "Medium one", "harga" :500000, "ketersediaan": 3},
    ]


    <<Kos=kosan disini menggunakan id sebagai identity mereka, sehingga apabila mealakukan update data ataupun penghapusan maka kita bisa langsung mencarinya dengan id mereka.>>
      <<Untuk keterangan kosan seperti ini:>>
      <<1. Luxury one : Kamar AC, kamar mandi dalam, ada fullset meja,lemari,kasur, kamar luas>>
      <<2.  Single room : Kamar sendiri, tidak AC,kamar mandi dalam,kamar luas, fullset meja,lemari,kasur>>
      <<3. Sharing room : Punya teman sekamar, tidak AC, kamar mandi luar, ranjang tingkat>>
      <<4. Medium one : single room, tidak AC, kamar mandi luar, kamar tidak luas, fullset kasur,meja,lemari biasa>>

    <Fungsi untuk menambahkan data>
     def Create_table(tipe, harga,ketersediaan):
        id_terakhir = kosan_rene[-1]["id"] if kosan_rene else 0
          new_id = id_terakhir + 1
            kosan_rene.append({"id": new_id, "tipe": tipe, "harga": harga, "ketersediaan": ketersediaan})
            print(f"Data dengan ID {new_id} berhasil ditambahkan.") 
    
    <<Maksud dari id_terakhir = kosan rene[-1][id] sebagaimana dalam list atau tuple posisi anggota list dari belakang adalah -1,-2,-3, jadi dengan menambahkan anggota tabel maka id terakhir misal 4, jika ditambah 4+1 = 5. Nah nanti outputnya akan secara langsung me- list 5 dalam tabel walau kita menulis 6 sekalipun>>

    <Fungsi untuk menampilkan tabel data>
    def Read_table():
    kosan_table.clear_rows()
    for row in kosan_rene:
        kosan_table.add_row([row["id"], row["tipe"], row["harga"], row["ketersediaan"]])
    print(kosan_table)
  
    <<Disini terdapat clear_rows untuk apa? Gunanya untuk menghapus table jika dijalankan. Nah karena jika kita tak memakai clear rows nantinya bentuk table kita bakal berantakan>>
    <<berantakan yang dimaksud seperti, misal id nanti dari 1,2,3,4 akan terulang lagi 1,2,3,4 seterusnya. Dengan clear_rows dia akan membuat urutan table menjadi rapi dan sesuai input admin.>>

    <Fungsi untuk mengupdate data berdasarkan ID>
    def update_table(id, tipe, harga):
      for row in kosan_rene:
        if row["id"] == id:
            row["tipe"] = tipe
            row["harga"] = harga
            print(f"Data dengan ID {id} berhasil diupdate.")
            return
        print(f"Data dengan ID {id} tidak ditemukan.")

    <Fungsi untuk menghapus data berdasarkan ID>
    def Delete_table(id):
        for row in kosan_rene:
          if row["id"] == id:
            kosan_rene.remove(row)
            print(f"Data dengan ID {id} berhasil dihapus.")
            return
        print(f"Data dengan ID {id} tidak ditemukan.")

    <Fungsi Untuk melakukan transaksi>
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

    <Program utama>
    if __name__ == "__main__":
        Password = "admini"
        <<Ini dimaksudkan sebagai program utama, the main program, sehingga ketika dijalankan pun program Option Admin dan User akan dijalankan pertama>>

    while True:
        Option = input('Anda masuk sebagai?(Admin/User):')

    if Option == 'Admin':
        Kode = input('Masukkan Kode Admin:')
        if Kode != Password : 
            print('wah ada yang salah')
            continue

        <Program Utama Admin>
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






![Screenshot (81)](https://github.com/IreneMNS/POST_TEST_2/assets/144671469/0040fe9a-428a-44d5-8148-94de3c48dedc)
Ini adalah contoh output dari ADMIN
![Screenshot (86)](https://github.com/IreneMNS/POST_TEST_2/assets/144671469/84a912e9-7504-4948-866d-50125443b18f)
Untuk gamabar di atas ini adalah sebuah output untuk program USER


![Screenshot (85)](https://github.com/IreneMNS/POST_TEST_2/assets/144671469/7ac7e3c5-13f5-4743-8c44-848e9644e998)
![Screenshot (84)](https://github.com/IreneMNS/POST_TEST_2/assets/144671469/3a61440c-9f27-4263-8819-58d4e2f712d1)
![Screenshot (83)](https://github.com/IreneMNS/POST_TEST_2/assets/144671469/732022d1-9b8c-4c87-a3a6-69fe3344a446)
![Screenshot (82)](https://github.com/IreneMNS/POST_TEST_2/assets/144671469/27bc74fb-2e0f-47e6-911c-500a5c36fb96)



    
