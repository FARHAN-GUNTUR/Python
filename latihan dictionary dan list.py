import os
os.system("cls")
# nama = input("Siapa nama Anda? : ")
# umur = int(input("Berapa usia anda? :"))
# tempat_tinggal = input("Dari mana anda berasal? :")
# data = {
#     "nama": nama,
#     "umur": umur,
#     "asal": tempat_tinggal,
# }
# print(data)
# data_mahasiswa = {}
# mahasiswa = {
#     "nama": input("Siapa Nama Anda :"),
#     "umur": int(input("Berapa Umur Anda :")),
#     "tempat_tinggal": input("Anda tinggal dimana ? :")
# }
# data_mahasiswa.update({'key': mahasiswa})
# for mahasiswa in data_mahasiswa:
#     nama = data_mahasiswa[mahasiswa]["nama"]
#     umur = data_mahasiswa[mahasiswa]["umur"]
#     tempat_tinggal = data_mahasiswa[mahasiswa]["tempat_tinggal"]
#     print(nama, umur, tempat_tinggal)

data_mahasiswa = []
while True:
    nama = input("Siapa nama anda ? : ")
    umur = int(input("Berapa Usia Anda ? : "))
    tempat_tinggal = input("Anda Tinggal dimana ? : ")
    data_diri = {
        # ?DATA DICTIONARY
        # !key : value
        'Nama': nama,
        'Usia': umur,
        'Asal': tempat_tinggal,
    }
    data_mahasiswa.append(data_diri)
    for index, mahasiswa in enumerate(data_mahasiswa):
        nama = mahasiswa.get('Nama')
        umur = mahasiswa.get('Usia')
        asal = mahasiswa.get('Asal')
        # print(
        #     f"{index+1}.) Nama : {mahasiswa['Nama']} Usia : {mahasiswa['Usia']} Asal : {mahasiswa['Asal']}")
        print(nama, umur, asal)

    # for index, i in enumerate(data_mahasiswa):
    #     print(f"{index+1}.) {i['Nama']} : {i['Usia']} : {i['Asal']}")
    # lanjut = input("Lanjutkan (y/n) : ")
    # if lanjut == "n":
    #     break
