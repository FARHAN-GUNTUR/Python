import datetime as dt


def sayHello(waktu, nama):
    kalimat = (f"Halo {nama}, Selamat {waktu}")
    print(kalimat)


sayHello('Pagi', 'Guntur')


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

# !NOMER 2


# !PENGULANGAN
# i = 0
# while i <= 10:
#     print(i)
#     i += 1
# print('=' * 25)

# for x in range(10):
#     if x % 2 == 1:
#         continue
#     print(x)
# print('=' * 25)

# noAngkot = 1
# jumlahAngkot = 10
# angkotBeroperasi = 6
# for (noAngkot) in range(jumlahAngkot + 1):
#     if noAngkot == 0:
#         continue
#     elif noAngkot <= angkotBeroperasi:
#         print(f'Angkot no. {noAngkot} sedang beroperasi')
#     else:
#         print(f'Angkot no. {noAngkot} sedang rusak')
