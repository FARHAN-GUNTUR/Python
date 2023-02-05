# dataList = ["Guntur", "Wahyu", "Septiaji",
#             "Farhan", "Tri", "Silvi", "Wulandari"]
# print(dataList)
# print("=" * 25)
# panjangData = len(dataList)
# print("=" * 25)
# print(f"Panjang datanya adalah {panjangData}")
# print("=" * 25)
# print(dataList[1:])
# print("=" * 25)
# print(dataList[:3])
# print("=" * 25)
# print(dataList[1:4])
# print(dataList[2:6])
# print("=" * 25)
# print(dataList[-3])
# print("=" * 25)
# print(dataList[-4:-1])
# dataList[3] = "Aku"
# print(dataList)

# listBuah1 = ["Apel", "Mangga", "Jeruk", "Pisang"]
# listBuah2 = ["Rambutan", "Salak", "Pepaya", "Nanas"]
# listBuah1.append("Jus Buah")  # ! MENAMBAHKAN JUS BUAH PADA AKHIR LIST BUAH 1
# ! MENAMBAHKAN CERRY PADA LIST BUAH 2 DENGAN INDEX KE 2
# listBuah2.insert(2, "Cerry")
# !MENGGABUNGKAN LIST BUAH 1 DENGAN LIST BUAH 2
# listBuah1.extend(listBuah2)
# !MENGURUTKAN LIST DARI HASIL PENGGABUNGAN LIST BUAH 1 DAN LIST BUAH 2
# listBuah1.sort()
# print(listBuah1)
# # !FOR LOOP
# # !CARA1
# for i in range(len(listBuah1)):
#     print(listBuah1[i])
# !CARA2
# ?LEBIH DISARANKAN MEMAKAI CARA YANG KEDUA
# for namaBuah in listBuah1:
#     print(namaBuah)
# for index, namaBuah in enumerate(listBuah1):
#     print(index+1, namaBuah)

# !WHILE LOOP
# namaBuah = 0
# while namaBuah < len(listBuah1):
#     print(f"Nama buah : {listBuah1[namaBuah]}")
#     namaBuah += 1
# !LIST COMPREHENSION
# !CARA 1
# buah = [x for x in listBuah1]
# print(buah)
# !CARA 2
# buah = [i for i in listBuah1]
# for index,x in range(len(buah)):
#     print(buah[x])
# !CARA 3
# buah = [i for i in listBuah1]
# for index, x in enumerate(buah):
#     print(index+1, x)
# print('=' * 20)
# !LIST COMPREHENSION DENGAN PENGKONDISIAN
# !CARA 1
# hasil = [x for x in listBuah1 if "a" in x]
# print(hasil)
# !CARA 2
# hasil = [x for x in listBuah1 if "a" in x]
# for i in range(len(hasil)):
#     print(hasil[i])
# !CARA 3
# hasil = [x for x in listBuah1 if "a" in x]
# for index, i in enumerate(hasil):
#     print(index+1, i)


# listBuah1 = ["Apel", "Mangga", "Jeruk", "Pisang"]
# listBuah2 = ["Rambutan", "Salak", "Pepaya", "Nanas"]
# listBuah1.append("Jus Buah")
# listBuah2.insert(2, "Cerry")
# listBuah1.extend(listBuah2)
# !MEMASUKKAN LIST BUAH 1 KE DALAM VARIABLE
# listTerbaru = listBuah1.copy()
# listTerbaru.sort()
# print(listTerbaru)
# !FOR LOOP
# !CARA 1
# for i in range(len(listTerbaru)):
#     print(listTerbaru[i])
# !CARA 2
# ?LEBIH DISARANKAN MENGGUNAKAN CARA YANG KEDUA
# for buah in listTerbaru:
#     print(buah)

# !WHILE LOOP
# i = 0
# while i < len(listTerbaru):
#     print(listTerbaru[i])
#     i += 1

# !LIST COMPREHENSION
# buah = [i for i in listTerbaru]
# print(buah)
# buah = [x for x in listTerbaru]
# for i in range(len(buah)):
#     print(buah[i])
# !LIST COMPREHENSION DENGAN PENGKONDISIAN
# nama = [a for a in listTerbaru if "c" in a]
# for i in range(len(nama)):
#     print(nama[i])

# perabotan1 = ["Tv", "Laptop", "Hp", "Smartwatch", "Google Lens", "Rice Cooker"]
# # ! Mengubah index ke 2 dan ke 3 serta menghilangkan index ke 3-5
# perabotan1[2:6] = ["Lampu", "Gadget"]
# perabotan1.append("Dinamo")
# print(perabotan1)
# !PENGULANGAN
# !1. WHILE LOOP
# i = 0
# while i < len(perabotan1):
#     print(perabotan1[i])
#     i += 1
# !2.FOR LOOP
# !CARA 1
# for x in range(len(perabotan1)):
#     print(perabotan1[x])
# !CARA 2
# for x in perabotan1:
    # print(x)


# ! LATIHAN LIST

listBuku = []
while True:
    judul = input("Judul Buku : ")
    penulis = input("Penulis\t : ")
    buku = {
        # ?DATA DICTIONARY
        # !key : value
        'Judul': judul,
        'Penulis': penulis}
    listBuku.append(buku)
    for index, i in enumerate(listBuku):
        print(f"{index+1}.) {i['Judul']} : {i['Penulis']}")
    lanjut = input("Lanjutkan (y/n) : ")
    if lanjut == "n":
        break
