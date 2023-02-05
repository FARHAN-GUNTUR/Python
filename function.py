# def sayHello(nama):
#     kalimat = f"Hello {nama}"
#     return kalimat


# print(sayHello("Guntur"))
# print("=" * 25)
# print("=" * 25)
# print("=" * 25)

# def sayHello(waktu, nama):
#     kalimat = f"Halo {nama}, Selamat {waktu}"
#     return kalimat


# print(sayHello("Pagi", "Guntur"))

# print("=" * 25)
# print("=" * 25)
# print("=" * 25)

# def sayHello(nama):
#     salam = []
#     for name in nama:
#         salam.append(f"Halo {name}")
#     return salam


# nama1 = ["Guntur", "Wahyu", "Septiaji", "Farhan"]
# ucapan = sayHello(nama1)
# for salam in ucapan:
#     print(salam)

# print("=" * 25)
# print("=" * 25)
# print("=" * 25)


# def sayHello(nama, waktu):
#     for i in nama:
#         for j in waktu:
#             print(f"Halo {i} Selamat {j}")
#             # print(f"Halo {nama[i]} Selamat {j}") #!TIDAK BISA MENGGUNAKAN INDEX


# list_nama = ["Guntur", "Wahyu", "Septiaji", "Farhan"]
# list_waktu = ["Pagi", "Siang", "Sore", "Malam"]
# sayHello(list_nama, list_waktu)

# print("=" * 25)
# print("=" * 25)
# print("=" * 25)


# def sayHello(nama, waktu):
#     for i in range(len(nama)):
#         for j in range(len(waktu)):
#             print(f"Halo {nama[i]} Selamat {waktu[j]}")


# list_nama = ["Guntur", "Wahyu", "Septiaji", "Farhan"]
# list_waktu = ["Pagi", "Siang", "Sore", "Malam"]
# sayHello(list_nama, list_waktu)


# print("=" * 25)
# print("=" * 25)
# print("=" * 25)
# def sayHello(nama, waktu):
#     for i in range(len(nama)):
#         print(f"Halo {nama[i]} Selamat {waktu[i]}")


# list_nama = ["Guntur", "Wahyu", "Septiaji", "Farhan"]
# list_waktu = ["Pagi", "Siang", "Sore", "Malam"]
# sayHello(list_nama, list_waktu)

# !DEFAULT PARAMETER VALUES
# def sayHello(nama="Farhan"):
#     kalimat = f"Halo {nama}"
#     print(kalimat)


# sayHello()

# print("=" * 25)
# print("=" * 25)
# print("=" * 25)

# def say(nama, waktu="Pagi"):
#     ucapan = f"Halo {nama} Selamat {waktu}"
#     print(ucapan)


# say("Guntur")
# say("Wahyu", "Malam")

# print("=" * 25)
# print("=" * 25)
# print("=" * 25)
# def buah(nama):
#     for i in nama:
#         print(i)


# list_buah = ["Anggur", "Nanas", "Apel", "Jeruk"]
# buah(list_buah)


# !MENGHENTIKAN SEBUAH FUNCTION
# !CONTOH PERTAMA
# def cari(angka1, angka2):
#     for temukan in angka1:
#         if temukan == angka2:
#             return True
#     return False


# pertama = [213, 1, 5, 6, 7, 2, 8, 9, 2, 215, 21, 313, 4]
# kedua = 9
# ketemu = cari(pertama, kedua)
# print(f"Angka yang anda cari adalah {kedua} = {ketemu}")

# !CONTOH KEDUA
# def cariBuah(buah1, buah2):
#     for cari in buah1:
#         if cari == buah2:
#             return True
#     return False


# once = ["Mangga", "Nanas", "Semangka", "Jambu", "Rambutan"]
# twice = "Cerry"
# temu = cariBuah(once, twice)
# print(f"Buah yang anda cari adalah {twice} dan buahnya adalah {temu}")
# !MENGHITUNG VOLUME DUA KUBUS
# def volumeDuaKubus(angka1, angka2):
#     hasil = angka1**3 + angka2**3
#     return hasil


# pertama = float(input("Sisi kubus 1 (cm) : "))
# kedua = float(input("Sisi kubus 2 (cm) : "))
# jumlah = volumeDuaKubus(pertama, kedua)
# print(f"Sisi kubus 1 adalah {pertama} (cm)")
# print(f"Sisi kubus 2 adalah {kedua} (cm)")
# print(f"Jumlah volume dua kubus tersebut adalah {jumlah} ")
