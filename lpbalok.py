print('## Program Menghitung Luas Permukaan Balok ##')
print ('====================================================')
Nama = 'Alti Vanie Diandra Eka Putri'
print('Nama:', Nama)
Nim = '2310432002'
print('Nim:', Nim)
Kelas = 'B'
print('Kelas:', Kelas)
print ('====================================================')
Panjang = float(input("Panjang="))
Lebar   = float(input("Lebar="))
Tinggi  = float(input("Tinggi="))
luas_permukaan = 2 * (Panjang * Lebar + Panjang * Tinggi + Lebar * Tinggi)
print("Luas permukaan balok dengan panjang", Panjang, ", lebar", Lebar, ", dan tinggi", Tinggi, "adalah:", luas_permukaan)