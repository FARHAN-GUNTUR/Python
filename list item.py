# names = ["mariya", "BATMAN", "superman"]
# nama = [n.capitalize() if n.islower() else "Relax " + n.capitalize() for n in names]
# print(nama)
# buah1 = ["Apel", "Mangga", "Jeruk", "Pisang", "jambu"]
# ?MEMBUAT TEKS MENJADI HURUF BESAR SEMUA DENGAN MENGGUNAKAN LIST COMPREHENSION
# buah = [i.upper() if i.capitalize() else i.upper() for i in buah1]
# print(buah)
# buah2 = ["Rambutan", "Salak", "Pepaya", "Nanas"]
# buah1.append("Kedondong")
# buah1.extend(buah2)
# print(buah1)

# ?jika kamu ingin menambahkan satu elemen ke dalam list, kamu harus menggunakan append, tetapi jika kamu ingin menambahkan seluruh elemen dari suatu list lain, kamu harus menggunakan extend.
# TODO: PENGULANGAN
# !WHILE LOOP
# i = 0
# while i < len(buah1):
#     print(buah1[i])
#     i += 1
# !FOR LOOP
# ? CARA 1
# for i in range(len(buah1)):
#     print(buah1[i])
# ? CARA 2
# for i in buah1:
#     print(i)
# ? CARA 3
# for index, i in enumerate(buah1):
#     print(index+1, i)
# for index, i in enumerate(buah1, start=1):
#     print(index, i)

# TODO: LIST COMPREHENSION
# ?TANPA PENGKONDISIAN
# !CARA 1
# buah = [i for i in buah1]
# print(buah)
# !CARA 2
# buah = [i for i in buah1]
# for x in buah:
# print(x)
# !CARA 3
# buah = [i for i in buah1]
# for x in range(len(buah)):
#     print(buah[x])
# !CARA 4
# buah = [i for i in buah1]
# for index, x in enumerate(buah):
#     print(index+1, x)
# buah = [i for i in buah1]
# for index, x in enumerate(buah, start=1):
#     print(index, x)
# ?DENGAN PENGKONDISIAN
# !CARA 1
# buah = [i for i in buah1 if "a" in i]
# print(buah)
# !CARA 2
# buah = [i for i in buah1 if "a" in i]
# for x in buah:
#     print(x)
# !CARA 3
# buah = [i for i in buah1 if "a" in i]
# for x in range(len(buah)):
#     print(buah[x])
# !CARA 4
# buah = [i for i in buah1 if "a" in i]
# for index, x in enumerate(buah):
# print(index+1, x)
# buah = [i for i in buah1 if "a" in i]
# for index, x in enumerate(buah, start=1):
#     print(index, x)
