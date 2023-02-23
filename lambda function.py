# !
# ?LAMBDA FUNCTIONS DAPAT DIGUNAKAN DALAM BANYAK SITUASI, TERGANTUNG PADA KEBUTUHAN MASING-MASING. NAMUN, SEPERTI YANG DISEBUTKAN SEBELUMNYA, MEREKA LEBIH BAIK DIGUNAKAN UNTUK TUGAS-TUGAS SEDERHANA DAN MUDAH DIBACA, DAN KURANG COCOK UNTUK KODE YANG LEBIH KOMPLEKS. DAN PERLU DIINGAT BAHWA PENGGUNAAN LAMBDA FUNCTION YANG TERLALU KOMPLEKS AKAN MENYULITKAN DALAM HAL PEMBACAAN DAN PEMELIHARAAN KODE. OLEH KARENA ITU, ADALAH LEBIH BAIK UNTUK MENGGUNAKAN FUNCTION BIASA KETIKA KODE MEMBUTUHKAN LOGIKA YANG LEBIH RUMIT.
# *LAMBDA FUNCTION
# !LAMBDA ARGUMENTS: EXPRESSION
# def number(x): return x+2


# newNUmber = number(10)
# print(f"Hasilnya = {newNUmber}")

# list_number = [1, 2, 3]
# number = list(map(lambda x: x**2, list_number))
# print(number)

# data_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# data_number1 = list(filter(lambda x: x % 2 == 1, data_number))
# print(data_number1)


# def nomer(n):
#     return lambda nomers: nomers**n


# nomers1 = nomer(3)(3)
# print(nomers1)



# def number(x): return x**2


# newNumber = number(10)
# print(f"Hasilnya adalah = {newNumber}")
# def number(x): return x**2


# ?----------------------------
# def newNumber(x):
#     hasil = [int(i)**2 for i in x]
#     return hasil


# number = input("Masukkan angka : ").split()
# print(newNumber(number))
# ?----------------------------


# TODO: MENGUBAH STRING MENJADI CAPITALIZE
# !CARA 1
# kalimat = "LAMBDA FUNCTIONS DAPAT DIGUNAKAN DALAM BANYAK SITUASI LAINNYA, TERGANTUNG PADA KEBUTUHAN MASING-MASING. NAMUN, SEPERTI YANG DISEBUTKAN SEBELUMNYA, MEREKA LEBIH BAIK DIGUNAKAN UNTUK TUGAS-TUGAS SEDERHANA DAN MUDAH DIBACA, DAN KURANG COCOK UNTUK KODE YANG LEBIH KOMPLEKS."
# ubah_kalimat = " ".join([i.capitalize() for i in kalimat.split()])
# print(ubah_kalimat)


# !CARA 2
# kalimat = "LAMBDA FUNCTIONS DAPAT DIGUNAKAN DALAM BANYAK SITUASI LAINNYA, TERGANTUNG PADA KEBUTUHAN MASING-MASING. NAMUN, SEPERTI YANG DISEBUTKAN SEBELUMNYA, MEREKA LEBIH BAIK DIGUNAKAN UNTUK TUGAS-TUGAS SEDERHANA DAN MUDAH DIBACA, DAN KURANG COCOK UNTUK KODE YANG LEBIH KOMPLEKS."
# ubah_kalimat = " ".join([i.capitalize() if i.isupper()
#                         else i.lower() for i in kalimat.split()])
# print(ubah_kalimat)


# !CARA 3
# def kata(x): return " ".join([i.capitalize() for i in x.split()])


# kata1 = kata("LAMBDA FUNCTIONS DAPAT DIGUNAKAN DALAM BANYAK SITUASI LAINNYA, TERGANTUNG PADA KEBUTUHAN MASING-MASING. NAMUN, SEPERTI YANG DISEBUTKAN SEBELUMNYA, MEREKA LEBIH BAIK DIGUNAKAN UNTUK TUGAS-TUGAS SEDERHANA DAN MUDAH DIBACA, DAN KURANG COCOK UNTUK KODE YANG LEBIH KOMPLEKS.")
# print(kata1)
