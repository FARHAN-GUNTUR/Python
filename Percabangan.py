# !OPERATOR TERNARY
# nilai = float(input('Nilai Anda : '))
# hasil = (f'Nilai anda {nilai}, Anda lulus') if nilai >= 80 else (
#     f'nilai anda {nilai}, Coba lagi tahun depan')
# print(hasil)

# !PERCABANGAN ELSE IF
# ! NOMER 1
# inputUser = float(input('Berapa nilai anda ? :'))
# ucapan = 'Nilai anda'
# if inputUser >= 90:
#     print(f'{ucapan} A')
# elif inputUser >= 80 and inputUser <= 90:
#     print(f'{ucapan} B+')
# elif inputUser >= 70 and inputUser <= 80:
#     print(f'{ucapan} B')
# elif inputUser >= 60 and inputUser <= 70:
#     print(f'{ucapan} C+')
# else:
#     print('Anda harus mengulang tahun depan')




# jumlahAngkot = 10
# angkotBeroperasi = 6
# noAngkot = 1
# while noAngkot <= angkotBeroperasi:
#     print(f"Angkot no. {noAngkot} sedang beroperasi")
#     noAngkot += 1
# for noAngkot in range(angkotBeroperasi, 11):
#     print(f"Angkot no. {noAngkot} sedang beroperasi")

# noAngkot = 11
# jumlahAngkot = 20
# angkotBeroperasi = 16
# for (noAngkot) in range(noAngkot, jumlahAngkot+1):
#     if noAngkot <= angkotBeroperasi:
#         print(f'Angkot no. {noAngkot} sedang beroperasi')
#     else:
#         print(f'Angkot no. {noAngkot} sedang rusak')

# noAngkot = 21
# jumlahAngkot = 30
# angkotBeroperasi = 26
# for noAngkot in range(noAngkot, jumlahAngkot+1):
#     if noAngkot == 24:
#         print(f"Angkot no. {noAngkot} berada di bengkel")
#     elif noAngkot <= angkotBeroperasi or noAngkot == 28:
#         print(f"Angkot no. {noAngkot} sedang beroperasi")
#     else:
#         print(f"Angkot no. {noAngkot} sedang rusak")

# jumlahAngkot = 30
# noAngkot = 1
# for i in range(noAngkot, jumlahAngkot+1):
#     if i in [16, 17, 18, 19, 20, 27, 28, 29, 30]:
#         print(f"Angkot no. {i} sedang rusak")
#     elif i == 24:
#         print(f"Angkot no. {i} sedang berada di bengkel")
#     else:
#         print(f"Angkot no. {i} sedang beroperasi")

# nama = "Guntur Wahyu Septiaji"
# ucapan = (
#     f"Selamat pagi {nama[:6]}") if "Guntur" in nama else "Good Job"
# print(ucapan)


# !KALKULATOR SEDERHANA
# angka1 = float(input("Angka Pertama : "))
# operator = input("Masukkan Operator ( + , - , / , x , ^s  ): ")
# angka2 = float(input("Angka Kedua : "))
# if operator == "+":
#     print(f"Hasilnya adalah {angka1 + angka2}")
# elif operator == "-":
#     print(f"Hasilnya adalah {angka1 - angka2}")
# elif operator == "/":
#     print(f"Hasilnya adalah {angka1 / angka2}")
# elif operator == "x" or operator == "*":
#     print(f"Hasilnya adalah {angka1 * angka2}")
# elif operator == "xx" or operator == "^" or operator == "**":
#     print(f"Hasilnya adalah {angka1 ** angka2}")
# else:
#     print("Jawabannya apa bang Messi?")


# def fizzBuzz(nilai):
#     for i in range(1, nilai+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

#     return nilai


# print(fizzBuzz(100))

