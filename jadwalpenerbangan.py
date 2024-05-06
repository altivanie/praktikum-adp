print('Program Tabel Jadwal Penerbangan Pesawat')
print()
print('****SELAMAT DATANG DI MASKAPAI VALEE AIR****')
print('Berikut adalah jadwal penerbangan yang tersedia')

jadwal_penerbangan = [
    ["Surabaya", "Jakarta", "09:30", "11:00"],
    ["Jakarta", "Bandung", "11:30", "13:00"],
    ["Surabaya", "Jakarta", "14:00", "15:20"],
    ["Jakarta", "Bandung", "15:30", "17:20"],
    ["Surabaya", "Jakarta", "18:00", "20.10"],
    ["Jakarta", "Bandung", "06:10", "07:10"],
    ["Padang", "Medan", "04.00", "05.00"],
    ["Padang", "Medan", "07:10", "08.40"],
    ["Padang", "Medan", "13:00", "15:00"],
]

print("\nJadwal Penerbangan:")
print("======================================================================")
print("| Kota Asal   | Kota Tujuan | Waktu Keberangkatan | Waktu Kedatangan |")
print("======================================================================")
for rute in jadwal_penerbangan:
    print(f"| {rute[0]:<12} | {rute[1]:<11} | {rute[2]:<19} | {rute[3]:<15} |")
print("======================================================================")

asal = input("Masukkan Kota Asal   = ").upper()
tujuan = input("Masukkan Kota Tujuan = ").upper()

rute_tercepat = None
waktu_tercepat = float('inf')

for rute in jadwal_penerbangan:
    if rute[0].upper() == asal and rute[1].upper() == tujuan:
        jam_keberangkatan = int(rute[2][:2])
        menit_keberangkatan = int(rute[2][3:])
        jam_kedatangan = int(rute[3][:2])
        menit_kedatangan = int(rute[3][3:])
        
        total_menit = (jam_kedatangan * 60 + menit_kedatangan) - (jam_keberangkatan * 60 + menit_keberangkatan)

        if total_menit < waktu_tercepat:
            waktu_tercepat = total_menit
            rute_tercepat = rute

if rute_tercepat:
    print("Rute tercepat dari",asal, "ke", tujuan, "adalah", rute_tercepat[2], "-", rute_tercepat[3],"WIB.")
else:
    print("Tidak ditemukan rute langsung dari", asal, "ke", tujuan)
