print('Program Caesar Cipher')
print('====================================================')
Nama = 'Alti Vanie Diandra Eka Putri'
print('Nama:', Nama)
Nim = '2310432002'
print('Nim:', Nim)
Kelas = 'B'
print('Kelas:', Kelas)
print('====================================================')

print('Selamat Datang di Caesar Cipher Program')

alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher = ""

teks = input('Masukkan teks: ').lower()
k = int(input('Masukkan nilai k : '))
if 1 <= k <= 26:
    for x in teks:
        if x in alphabet:
            cipher += alphabet[(alphabet.index(x) + k) % 26]
        else:
            cipher += x
    print('Hasil enkripsi teks adalah:', cipher)
else:
    print('Nilai k harus dalam rentang 1-26. Program tidak dapat melanjutkan')
