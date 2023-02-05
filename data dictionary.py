# dataDict = {
#     #! "Key": "value",
#     "name": "Guntur",
#     "tahun": 2002,
#     "asal": "Malang",
#     "warna": ["Red", "Green", "Blue"]
# }

# print(dataDict)
# print(dataDict.setdefault("warna"))
# kalimat = "Senang Sekali" if "name" in dataDict else "Biasa saja"
# print(kalimat)
# ! APABILA ADA MAKA AKAN MENGHASILKAN NILAI TRUE
# cek = "nama" in dataDict
# print(cek)
# !MENGAKSESS VALUE
# !CARA 1
# print(dataDict["name"])
# data = dataDict["asal"]
# print(data)
# !CARA 2 DENGAN MENGGUNAKAN METHOD GET
# data2 = dataDict.get("tahun")
# print(data2)
# warna = dataDict.get("warna")
# print(warna)
# !MENGHITUNG PANJANG DARI DATA DICTIONARY
# print(len(dataDict))
# ?ACCESS ITEMS DATA DICTIONARY
# !MENAMPILKAN KEY
# dict2 = dataDict.keys()
# print(dict2)
# !MENAMPILKAN SEMUA VALUES
# dict3 = dataDict.values()
# print(dict3)
# !MENAMBAHKAN ITEMS PADA DATA DICTIONARY
# !CARA 1
# dataDict["umur"] = 20
# print(dataDict)
# !CARA 2
# dataDict.update({"umur": 20})
# print(dataDict)
# !MENGHAPUS ITEMS PADA DATA DICTIONARY
# !CARA 1
# !DENGAN MENGGUNAKAN METHOD POP
# dataDict.pop("asal")
# print(dataDict)
# !CARA 2
# !DENGAN MENGGUNAKAN POP ITEMS, AKAN MENGHAPUS ITEMS YANG TERAKHIR PADA DATA DICTIONARY
# !AKAN BERJALAN PADA VERSI 3.7 KEBAWAH
# dataDict.popitems()
# print(dataDict)
# !CARA 3
# !MENGGUNAKAN METHOD DELETE
# del dataDict["name"]
# print(dataDict)
# !CARA 4
# !DENGAN MENGGUNAKAN METHOD CLEAR
# !AKAN MENGHAPUS SEMUA ITEMS YANG ADA PADA DATA DICTIONARY
# dataDict.clear()
# print(dataDict)


# TODO: LOOPING DATA DICTIONARY
# dataDict = {
#     #! "Key": "value",
#     "name": "Guntur",
#     "tahun": 2002,
#     "asal": "Malang",
#     "warna": ["Red", "Green", "Blue"]
# }
# !MENAMPILKAN KEY
# ! CARA 1
# for i in dataDict:
#     print(i)
# !CARA 2
# ?LEBIH DISARANKAN MENGGUNAKAN CARA YANG KEDUA
# for i in dataDict.keys():
#     print(i)

# !MENAMPILKAN VALUE
# ?DISARANKAN MENGGUNAKAN CARA YANG KEDUA ATAU KETIGA
# !CARA 1
# for i in dataDict:
#     print(dataDict[i])
# !CARA 2
# for i in dataDict.values():
#     print(i)
# !CARA 3
# for i in dataDict.keys():
#     print(dataDict.get(i))
# !MENAMPILKAN ITEMS
# !CARA 1
# for a in dataDict.items():
#     print(a)
# !CARA 2
# ? for key, value in dataDict.items():
# for a, b in dataDict.items():
#     print(f"{a} : {b}")

# TODO: COPY DATA DICTIONARY
# dataDict = {
#     #! "Key": "value",
#     "name": "Guntur",
#     "tahun": 2002,
#     "asal": "Malang",
#     "warna": ["Red", "Green", "Blue"]
# }
# print(dataDict)
# # !CARA 1
# dictCopy = dataDict.copy()
# print(dictCopy)
# # !CARA 2
# dictCopy2 = dict(dataDict)
# print(dictCopy2)
# dictCopy["suka"] = "susu"
# print(dictCopy)
# dictCopy.update({"hp": "Samsung"})
# print(dictCopy)
# print(dictCopy["hp"])

# TODO: NESTED DICTIONARIES
# myfamily = {
#     "child1": {
#         "name": "Emil",
#         "year": 2004
#     },
#     "child2": {
#         "name": "Tobias",
#         "year": 2007
#     },
#     "child3": {
#         "name": "Linus",
#         "year": 2011
#     }
# }
# for keluarga in myfamily:
#     nama = myfamily[keluarga]["name"]
#     tahun = myfamily[keluarga]["year"]
#     print(f"Nama saya {nama} dan lahir pada tahun {tahun}")


mahasiswa1 = {
    "nama": "Guntur",
    "nilai": 80,
    "univ": "Brawijaya"
}
mahasiswa2 = {
    "nama": "Farhan",
    "nilai": 85,
    "univ": "Malang"
}
mahasiswa3 = {
    "nama": "Wahyu",
    "nilai": 90,
    "univ": "Poltek"
}
mahasiswa = {
    "mahasiswa1": mahasiswa1,
    "mahasiswa2": mahasiswa2,
    "mahasiswa3": mahasiswa3
}
for data in mahasiswa:
    nama = mahasiswa[data]["nama"]
    nilai = mahasiswa[data]["nilai"]
    univ = mahasiswa[data]["univ"]
    print(f"Nama = {nama}, nilai = {nilai}, univ = {univ}")


