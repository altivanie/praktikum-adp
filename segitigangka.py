print('Program Mencetak Pola Segitiga Angka')
print('====================================================')
Nama = 'Alti Vanie Diandra Eka Putri'
print('Nama:', Nama)
Nim = '2310432002'
print('Nim:', Nim)
Kelas = 'B'
print('Kelas:', Kelas)
print('====================================================')

n = int(input("Masukkan tinggi segitiga: "))

if n >= 1:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
else:
    print("Terjadi kesalahan")



    

