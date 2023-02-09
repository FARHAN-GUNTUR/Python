
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
# ?
# def sayHello(nama, waktu):
#     for i in range(len(nama)):
#         print(f"Halo {nama[i]} Selamat {waktu[i]}")


# list_nama = ["Guntur", "Wahyu", "Septiaji", "Farhan"]
# list_waktu = ["Pagi", "Siang", "Sore", "Malam"]
# sayHello(list_nama, list_waktu)
def sayHello(nama, waktu):
    for names, times in zip(nama, waktu):
        print(f"Halo {names} Selamat {times}")


list_nama = ["Guntur", "Wahyu", "Septiaji", "Farhan"]
list_waktu = ["Pagi", "Siang", "Sore", "Malam"]
sayHello(list_nama, list_waktu)

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

# TODO: *ARGS PADA PYTHON
# def jumlah(*number):
#     hasil = 0
#     for angka in number:
#         hasil += angka
#     return hasil


# nomer = jumlah(1, 2, 3, 4, 5)
# print(nomer)


# def nama_lengkap(*name):
#     for index, nama in enumerate(name):
#         print(f"{index+1}.{nama}")


# first = nama_lengkap("Farhan", "Guntur")


# TODO: **KWARGS PADA
# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")


# print_kwargs(first_name="John", last_name="Doe")
# print_kwargs(first_name="FARHAN", last_name="GUNTUR")
# enter = dict(input("Masukkan nama: "))
# print_kwargs(enter)


# def print_values(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")


# while True:
#     input_data = input(
#         "Enter values in key=value format, separated by comma: ")
#     data = dict(item.split("=") for item in input_data.split(","))

#     print_values(**data)
#     lanjut = input("Mau Lanjut Bro? (y/n) : ")
#     if lanjut == "y":
#         continue
#     else:
#         break


# def print_student_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# student1 = {
#     "first_name": "John",
#     "last_name": "Doe",
#     "age": 25,
#     "major": "Computer Science"
# }

# student2 = {
#     "first_name": "Jane",
#     "last_name": "Doe",
#     "age": 23,
#     "major": "Mathematics"
# }

# student3 = {
#     "first_name": "Guntur",
#     "last_name": "Farhan",
#     "age": 20,
#     "major": "Pysics"
# }

# print("Student 1 Info:")
# print_student_info(**student1)

# print("\nStudent 2 Info:")
# print_student_info(**student2)

# print("\nStudent 3 Info:")
# print_student_info(**student3)

# def calculator (a,operator,b):
#   if operator == "+":
#     return a+b
