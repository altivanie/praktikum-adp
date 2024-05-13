kegiatan = []

def tambah_kegiatan():
    kegiatan_nama = input('Silahkan masukkan kegiatan anda: ')
    waktu_mulai = float(input('Masukkan waktu mulai: '))
    waktu_selesai = float(input('Masukkan waktu selesai: '))
    deskripsi = input('Masukkan deskripsi: ')
    kegiatan_baru = { 
        'Nama': kegiatan_nama,
        'Waktu mulai': waktu_mulai,
        'Waktu selesai': waktu_selesai,
        'Deskripsi': deskripsi
    }
    kegiatan.append(kegiatan_baru)
    print('Kegiatan berhasil ditambahkan.')

def tampilkan_kegiatan():
    if not kegiatan:
        print('Maaf tidak ada kegiatan yang dapat ditampilkan')
    else:
        print('Kegiatan saat ini:')
        print('{:<5} {:<20} {:<10} {:<10} {:<30}'.format('No', 'Nama Kegiatan', 'Mulai', 'Selesai', 'Deskripsi'))
        print('-' * 75)
        for index, kegiatan_item in enumerate(kegiatan, start=1):
            print(f'{index:<5} {kegiatan_item["Nama"]:<20} {kegiatan_item["Waktu mulai"]:<10.2f} {kegiatan_item["Waktu selesai"]:<10.2f} {kegiatan_item["Deskripsi"]:<30}')

def hapus_kegiatan():
    if not kegiatan:
        print('Tidak ada kegiatan yang dapat dihapus.')
    else:
        kegiatan_index = int(input('Masukkan nomor kegiatan yang ingin anda hapus: '))
        if 1 <= kegiatan_index <= len(kegiatan):
            del kegiatan[kegiatan_index - 1]
            print('Kegiatan berhasil dihapus.')
        else:
            print('Nomor kegiatan tidak valid.')

print('Selamat Datang di Program To Do List')
while True:
    print('Daftar Menu:')
    print('1. Tambah kegiatan')
    print('2. Tampilkan kegiatan')
    print('3. Hapus kegiatan')
    print('4. Keluar')
    menu = input('Silahkan Pilih Menu yang Tersedia: ')

    if menu == '1':
        tambah_kegiatan()
    elif menu == '2':
        tampilkan_kegiatan()
    elif menu == '3':
        hapus_kegiatan()
    elif menu == '4':
        print('Terima kasih telah menggunakan program ini.')
        break
    else:
        print('Pilihan Menu tidak valid. Silahkan coba lagi.')
