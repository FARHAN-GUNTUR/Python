# !
# TODO: LIST COMPREHENSION
# ! NOMER 1 TANPA PENGKONDISIAN
# ! CARA 1
# ? TANPA MENGGUNAKAN LIST COMPREHENSION
# fruits = ["apel", "mangga", "jeruk", "pisang", "jambu"]
# fruit = []
# for f in fruits:
#     f = f.upper()
#     fruit.append(f)
# fruits = fruit
# print(fruits)
# ! CARA 2
# ? DENGAN MENGGUNAKAN LIST COMPREHENSION
# fruits = ["apel", "mangga", "jeruk", "pisang", "jambu"]
# fruit = [f.upper() for f in fruits]
# print(fruit)


# ! NOMER 2 DENGAN PENGKONDISIAN
# ? TANPA MENGGUNAKAN LIST COMPREHENSION
# cek = [True, False, False, False, True, False, False, False, True, True, False]
# cek_benar = []
# for c in cek:
#     if c == True:
#         cek_benar.append(1)
#     else:
#         cek_benar.append(0)
# # cek = cek_benar
# print(cek)
# print(cek_benar)
# ? TANPA MENGGUNAKAN LIST COMPREHENSION
# cek = [True, False, False, False, True, False, False, False, True, True, False]
# benar = [1 if c == True else 0 for c in cek]
# print(cek)
# print(benar)

# ! NOMER MEMANIPULASI STRING
# nama = "HaloNamaSayaGunturWahyuSeptiaji"
# nama_benar = "".join([i if i.islower() else " " + i.lower() if i in ["N", "S"] else " " + i for i in nama])[1:]
# print(nama)
# print(nama_benar)

names = ["mariya", "BATMAN", "superman"]
# nama = [n.capitalize() if n.islower() else "Relax " + n.capitalize() for n in names]
nama = [n.capitalize() if n.islower() else n.lower() for n in names]
# nama = [n.capitalize() if n.islower() else "Halo " + n.upper() for n in names]
print(nama)

