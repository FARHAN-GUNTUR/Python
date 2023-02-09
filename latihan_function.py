# !
# TODO: MENGHITUNG LUAS DAN KELILING PERSEGI PANJANG


# def header():

#     os.system("cls")
#     print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
#     print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
#     print(f"{'1. UNTUK MENGHITUNG LUAS' :^40}")
#     print(f"{'2. UNTUK MENGHITUNG KELILING' :^40}")
#     print(f"{'3. UNTUK MENGHITUNG LUAS DAN KELILING' :^40}")
#     print(f"{'-'*40:^40}")


# def input_user():
#     '''input user'''
#     panjang = int(input("Masukkan nilai panjang: "))
#     lebar = int(input("Masukkan lebar: "))
#     return panjang, lebar


# def hitung_luas(panjang, lebar):
#     return panjang*lebar


# def hitung_keliling(panjang, lebar):
#     return 2*(panjang+lebar)


# def pesan(message, value):
#     print(f"Hasil perhitungan {message} adalah = {value}")


# while True:
#     header()
#     PANJANG, LEBAR = input_user()
#     luas = hitung_luas(PANJANG, LEBAR)
#     keliling = hitung_keliling(PANJANG, LEBAR)
#     pesan("Luas", luas)
#     pesan("Keliling", keliling)
#     lanjut = input("Apakah anda ingin lanjut ? (y/n) : ")
#     if lanjut == 'n':
#         break

# print("Thanks Bro")
# while True:
#     header()
#     opsi = int(input("Pilih 1, 2, 3: "))
#     if opsi == 1:
#         PANJANG, LEBAR = input_user()
#         luas = hitung_luas(PANJANG, LEBAR)
#         pesan("Luas", luas)
#     elif opsi == 2:
#         PANJANG, LEBAR = input_user()
#         keliling = hitung_keliling(PANJANG, LEBAR)
#         pesan("Keliling", keliling)
#     elif opsi == 3:
#         PANJANG, LEBAR = input_user()
#         luas = hitung_luas(PANJANG, LEBAR)
#         keliling = hitung_keliling(PANJANG, LEBAR)
#         pesan("Luas", luas)
#         pesan("Keliling", keliling)
#     else:
#         print("Pilihan yang salah bro")
#     isLanjut = input("Apakah anda ingin melanjutkan ? (y/n) :")
#     if isLanjut == "y":
#         continue
#     elif isLanjut == "n":
#         break
#     else:
#         break
# print("Thanks Bro")

# TODO: MENGHITUNG JUMLAH VOLUME DUA KUBUS

# def volumeDuaKubus(angka1, angka2):
#     hasil = angka1**3 + angka2**3
#     return hasil


# pertama = float(input("Sisi kubus 1 (cm) : "))
# kedua = float(input("Sisi kubus 2 (cm) : "))
# jumlah = volumeDuaKubus(pertama, kedua)
# print(f"Sisi kubus 1 adalah {pertama} (cm)")
# print(f"Sisi kubus 2 adalah {kedua} (cm)")
# print(f"Jumlah volume dua kubus tersebut adalah {jumlah} ")

# TODO: PROGRAM INPUT NAMA
# def header():
#     print(f"{'PROGRAM INPUT NAMA' :^40}")
#     print(f"{'-'*40:^40}")


# def input_user():
#     nama = input("Masukkan Nama : ")
#     umur = int(input("Berapa Umur Kamu? : "))
#     hoby = input("Apa Hoby Kamu? : ")
#     return (nama, umur, hoby)


# def pesan(name, age, hoby):
#     print(f"Nama : {name}\nUmur : {age}\nHoby : {hoby}")


# while True:
#     header()
#     NAMA, UMUR, HOBY = input_user()
#     pesan(NAMA, UMUR, HOBY)

#     print(f"{'='*40:^40}")
#     lanjut = input("Mau Lanjut Bro ? (y/n) : ")
    # if lanjut == "n":
    #     break

# TODO: PROGRAM UNTUK MENGHITUNG NILAI RATA-RATA DARI SUATU BILANGAN
# !CARA 1
# def rata_rata(angka):
#     hasil = 0
#     for i in angka:
#         hasil += i
#     return hasil / len(angka)


# satu = [1, 2, 3, 4, 5]
# print(rata_rata(satu))

# !CARA2
# !MENERIMA INPUT DARI USER
# def rata_rata(angka):
#     hasil = 0
#     for i in angka:
#         hasil += i
#     return hasil / len(angka)


# number = [int(x) for x in input("Masukkan Angka : ").split("+")]
# hasil = rata_rata(number)
# print(f"Rata-Rata dari {number} adalah {hasil}")




# !CARA 3
# !MENERIMA INPUT DARI USER DAN AKAN DIULANGI SECARA TERUS MENERUS
# def rata_rata(angka):
#     jumlah = 0
#     for i in angka:
#         jumlah += i
#     return jumlah / len(angka)


# def display(bilangan):
#     rata_rata(bilangan)
#     print(f"Rata-Rata Dari {number} = {result}")


# while True:
#     number = [int(x) for x in input("Masukkan Angka : ").split("+")]
#     result = rata_rata(number)
#     display(number)
#     terus = input("Mau Melanjutkan? (y/n): ")
#     if terus == "y":
#         continue
#     else:
#         break


# TODO: PROGRAM UNTUK MENENTUKAN FAKTORIAL DARI SUATU BILANGAN
# !CARA 1
# def faktorial(angka):
#     if angka == 0:
#         return 1
#     else:
#         return angka * faktorial(angka - 1)


# hasil = faktorial(5)
# print(f"Faktorial dari 5 = {hasil} ")

# !CARA2
# !MENERIMA INPUT DARI USER
# def faktorial(angka):
#     if angka == 0:
#         return 1
#     else:
#         return angka * faktorial(angka-1)


# angka1 = int(input("Masukkan Bilangan : "))
# hasil = faktorial(angka1)
# print(f"Faktorial dari {angka1} adalah {hasil}")

# !CARA 3
# !MENERIMA INPUT DARI USER DAN AKAN DIULANGI SECARA TERUS MENERUS
# def faktorial(angka):
#     if angka == 0:
#         return 1
#     else:
#         return angka * faktorial(angka-1)


# def pesan(bilangan):
#     jumlah = faktorial(bilangan)
#     print(f"Faktorial dari {bilangan} = {jumlah}")


# while True:
#     angka1 = int(input("Masukkan Angka : "))
#     hasil = faktorial(angka1)
#     pesan(angka1)
#     isLanjut = input("Mau Mencoba Angka Lain? (y/n) : ")
#     if isLanjut == "y":
#         continue
#     else:
#         break

# TODO: PROGRAM UNTUK MENENTUKAN APAKAH SUATU BILANGAN MERUPAKAN BILANGAN PRIMA ATAU BUKAN

# !CARA 1
# def prima(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# angka = 7
# if prima(angka):
#     print(f"{angka} adalah bilangan prima")
# else:
#     print(f"{angka} bukan bilangan prima")

# !CARA2
# !MENERIMA INPUT DARI USER
# def prima(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# angka = int(input("Masukkan Angka : "))
# hasil = prima(angka)
# if prima(angka):
#     print(f"{angka} adalah bilangan prima")
# else:
#     print(f"{angka} bukan bilangan prima")

# !CARA 3
# !MENERIMA INPUT DARI USER DAN AKAN DIULANGI SECARA TERUS MENERUS

# def prima(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# def tampil(bilangan):
#     prima(bilangan)
#     if prima(bilangan):
#         print(f"{bilangan} adalah bilangan prima")
#     else:
#         print(f"{bilangan} bukan bilangan prima")


# while True:
#     angka = int(input("Masukkan Angka : "))
#     hasil = prima(angka)
#     tampil(angka)
#     print(f"{'-'*40:^40}")
#     lanjut = input("Coba angka yang lain? (y/n) : ")
#     if lanjut == "y":
#         continue
#     else:
#         break
