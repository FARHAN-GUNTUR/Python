buah1 = ["Apel", "Mangga", "Jeruk", "Pisang"]
buah2 = ["Rambutan", "Salak", "Pepaya", "Nanas"]
buah1.extend(buah2)
# print(buah1)
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
