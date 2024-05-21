Nama = 'Alti Vanie Diandra Eka Putri'
print('Nama:', Nama)
Nim = '2310432002'
print('Nim:', Nim)
Kelas = 'B'
print('Kelas:', Kelas)
print()

def tambah_data(data):
    film = input("Masukkan Judul film: ")
    tanggal_menonton = input("Masukkan Tanggal Saat Mulai Menonton (format xx-yy-zzzz): ")
    nama_penulis = input("Masukkan Nama Penulis Skenario: ")
    nama_sutradara = input("Masukkan Nama Sutradara: ")
    tahun_rilis = int(input("Masukkan Tahun Rilis: "))
    
    data[film] = {
        'film': film,
        'tanggal_menonton': tanggal_menonton,
        'nama_penulis': nama_penulis,
        'nama_sutradara': nama_sutradara,
        'tahun_rilis': tahun_rilis,
    }
    
    with open("database.txt", "a") as file:
        file.write(f"{film},{tanggal_menonton},{nama_penulis},{nama_sutradara},{tahun_rilis}\n")
    print("Data film berhasil ditambahkan.")

def hapus_data(indeks):
    with open("database.txt", "r") as file:
        lines = file.readlines()
    with open("database.txt", "w") as file:
        for i, line in enumerate(lines):
            if i != indeks - 1:  
                file.write(line)
    print("Data telah berhasil dihapus!")

def tampil_data():
    with open("database.txt", "r") as file:
        lines = file.readlines()
        print('{:<5} {:<20} {:<20} {:<20} {:<20} {:<15}'.format('No', 'Judul Film', 'Tanggal Menonton', 'Nama Penulis', 'Nama Sutradara', 'Tahun Rilis'))
        print('-' * 100)
        for index, line in enumerate(lines, start=1):
            data = line.strip().split(',')
            print('{:<5} {:<20} {:<20} {:<20} {:<20} {:<15}'.format(index, data[0], data[1], data[2], data[3], data[4]))

print('Selamat Datang di Program Penyimpanan Data Film yang Telah Anda Tonton')
data = {}
while True:
    print('Menu Database Film')
    print("1. Tambah Data Film")
    print("2. Hapus Data Film")
    print("3. Tampilkan Data Film")
    print("4. Keluar dari program")
    
    menu = int(input("Masukkan nomor menu : "))
    if menu == 1:
        tambah_data(data)
    elif menu == 2:
        tampil_data()  
        hapus_indeks = int(input("Masukkan nomor data yang ingin dihapus: "))
        hapus_data(hapus_indeks)
    elif menu == 3:
        print("Data Film yang Sudah Anda Tonton")
        tampil_data()
    elif menu == 4:
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Nomor menu yang anda pilih tidak valid")
