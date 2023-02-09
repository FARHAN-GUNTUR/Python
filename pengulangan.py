# !PENGULANGAN
# ! 1.WHILE LOOP
# i = 0
# while i <= 10:
#     print(i)
#     i += 1
# print('=' * 25)


# ! 2.FOR LOOP
# ! CARA 1
# for x in range(0, 20, 2):  # range (start, end, step)
# print(x)

# ! CARA 2
# nomer = [i for i in range(0, 10)]
# print(nomer)


# for x in range(10):
#     if x % 2 == 1:
#         continue
#     print(x)

# kata = "Hello World!"
# for idx, i in enumerate(range(10)):
#     print(idx, kata)


# TODO:MENGHITUNG JUMLAH ANGKA
# !CARA 1
# angka = [1, 2, 3, 4, 5]
# hasil = 0
# for i in angka:
#     hasil += i
# print(hasil)
# # !CARA2
# angka = [1, 2, 3, 4, 5]
# hasil = sum(angka)
# print(hasil)


# !CARA3

# angka = [int(i) for i in input("Masukkan angka : ").split("+")]
# hasil = sum(angka)
# print(hasil)
# print(f"Hasil dari penjumlaha {angka} = {hasil}")

# !CARA 4

# while True:
#     angka = [int(i) for i in input("Masukkan angka : ").split("+")]
#     hasil = sum(angka)  # !SUM ADALAH PENJUMLAHAN
#     print(hasil)
#     print(f"Hasil dari penjumlaha {angka} = {hasil}")
#     lanjut = input("Anda mau lanjut? (y/n) : ")
#     if lanjut == "y":
#         continue
#     else:
#         break


# !MENGHITUNG RATA-RATA DARI PENJUMLAHAN BEBERAPA BILANGAN
# angka = [int(i) for i in input("Masukkan angka : ").split("+")]
# hasil1 = sum(angka)
# hasil2 = hasil1 / len(angka)
# print(f"Hasil dari rata-rata {angka} = {hasil2}")


# list_nama = ["Guntur", "Wahyu", "Septiaji", "Farhan"]
# list_waktu = ["Pagi", "Siang", "Sore", "Malam"]

# my_dict = {}
# for (key, val) in zip(list_nama, list_waktu):
#     my_dict[key] = val
# print(my_dict)
# for name, time in zip(list_nama, list_waktu):
#     print(f"Halo {name} Selamat {time}")

# for i in range(4):
#   my_dict[list_nama[i]] = list_waktu[i]
# print(my_dict)

# for i in range(len(list_nama)):
#     my_dict[list_nama[i]] = list_waktu[i]
# print(my_dict)
