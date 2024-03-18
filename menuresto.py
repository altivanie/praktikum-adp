print('Program Pemesanan Restoran')
print ('====================================================')
Nama = 'Alti Vanie Diandra Eka Putri'
print('Nama:', Nama)
Nim = '2310432002'
print('Nim:', Nim)
Kelas = 'B'
print('Kelas:', Kelas)
print ('====================================================')
print('Selamat Datang Di Valee Restaurant, Silahkan Memilih Menu yang Anda Inginkan')
print('Jenis Pesanan:')
print('1. Makanan')
print('2. Minuman')

Jenis_Pesanan = int(input('Pilih jenis pesanan: '))
if Jenis_Pesanan == 1:
    print('Menu Makanan:')
    print('1. Mie Ayam : Rp 12000')
    print('2. Ayam Penyet : Rp 13000')
    print('3. Pecel Lele : Rp 10000 ')

    Pilihan_Makanan = int(input('Pilih Nomor Menu Makanan: '))
    harga = 0
    if Pilihan_Makanan == 1:
        harga = 12000
    elif Pilihan_Makanan == 2:
        harga = 13000
    elif Pilihan_Makanan == 3:
        harga = 10000
    else:
        print('Kode Menu Tidak Valid')

    jumlah = int(input('Jumlah pesanan: '))
    Total_Harga = jumlah * harga
    print(f'Pesanan: No {Pilihan_Makanan}, Jumlah: {jumlah}, Total Harga: Rp {Total_Harga}')

elif Jenis_Pesanan == 2:
    print('Menu Minuman:')
    print('1. Jus Jambu : Rp 7000')
    print('2. Vanilla Latte : Rp 10000')
    print('3. Es Teh : Rp 5000')

    Pilihan_Minuman = int(input('Pilih Nomor Menu Minuman: '))
    harga = 0
    if Pilihan_Minuman == 1:
        harga = 7000
    elif Pilihan_Minuman == 2:
        harga = 10000
    elif Pilihan_Minuman == 3:
        harga = 5000
    else:
        print('Kode Menu Tidak Valid')

    jumlah = int(input('Jumlah pesanan: '))
    Total_Harga = jumlah * harga
    print(f'Pesanan: {Pilihan_Minuman}, Jumlah: {jumlah}, Total Harga: Rp {Total_Harga}')

    print('Terimakasih Telah Memesan di Valee Restaurant, Makanan Anda akan Segera Disiapkan')
