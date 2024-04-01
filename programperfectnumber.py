print('Program Menentukan Suatu Bilangan Termasuk Bilangan Sempurna dan Ganjil/Genap')
print('====================================================')
Nama = 'Alti Vanie Diandra Eka Putri'
print('Nama:', Nama)
Nim = '2310432002'
print('Nim:', Nim)
Kelas = 'B'
print('Kelas:', Kelas)
print('====================================================')

n = int(input('Masukkan bilangan: '))

print('Faktor dari', n, 'adalah:', end=' ')
jumlah = 0
for i in range (1, n):
    if n % i == 0:
        print(i, end=" ")
        jumlah += i

if jumlah == n:
    print("\n", n, "adalah bilangan sempurna") 
else:
    print("\n", n, "bukan bilangan sempurna") 

if n % 2 == 0:  
    tipe = 'genap'
else:
    tipe = 'ganjil'

print(n, 'merupakan bilangan', tipe)
