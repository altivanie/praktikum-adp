print('Program Tabel Penjumlahan dan Perkalian')
print('====================================================')
Nama = 'Alti Vanie Diandra Eka Putri'
print('Nama:', Nama)
Nim = '2310432002'
print('Nim:', Nim)
Kelas = 'B'
print('Kelas:', Kelas)
print('====================================================')

repeat = True
while repeat:
    print('\nSelamat Datang Di Program Penjumlahan dan Perkalian, Silahkan Pilih Menu di Bawah ini')
    print('Menu')
    print('1. Tabel Penjumlahan')
    print('2. Tabel Perkalian')
    print('3. Keluar')

    menu = input("Pilih menu: ")

    if menu == '1':
        print("Tabel Penjumlahan")
        n = int(input("Masukkan nilai n : "))
        if 1 <= n <= 10:
            print("\nTabel Penjumlahan", n, "x", n)
            print("   ", end="")
            for i in range(1, n + 1):
                print("{:4}".format(i), end=" ")
            print("\n-----------------------------------------------------")

            for i in range(1, n + 1):
                print("{:2} |".format(i), end="")
                for z in range(1, n + 1):
                    result = i + z
                    print("{:4}".format(result), end=" ")
                print()
        else:
            print("Masukkan nilai n sesuai rentang 1-10")

    elif menu == '2':
        print("Tabel Perkalian")
        n = int(input("Masukkan ukuran tabel perkalian: "))
        if 1 <= n <= 10:
            print("\nTabel Perkalian", n, "x", n)
            for i in range(1, n + 1):
                for z in range(1, n + 1):
                    result = i * z
                    print("{:3}".format(result), end=" ")
                print()
        else:
            print("Masukkan nilai n sesuai rentang 1-10")

    elif menu == '3':
        print("Anda akan segera keluar dari program")
        repeat = False

    else:
        print("Maaf pilihan anda tidak dapat kami proses")

 