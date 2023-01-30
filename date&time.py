import datetime as dt
print("Masukkan tanggal, bulan, dan tahun lahir anda")
tanggal = int(input("Tanggal :"))
bulan = int(input("Bulan :"))
tahun = int(input("Tahun :"))
tanggalLahir = dt.date(tahun, bulan, tanggal)
print(tanggalLahir)
hariIni = dt.date.today()
umurHari = hariIni - tanggalLahir
umurBulan = (umurHari.days % 365) // 30
umurTahun = umurHari.days // 365
print(f"Hari lahir anda : {tanggalLahir:%A}")
print(f"Umur anda adalah : {umurTahun} tahun, {umurBulan} bulan")
print(f"dan Anda hidup di dunia selama {umurHari}")
