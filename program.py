# from sty import fg
def input_user():
    nama = input("Masukkan Nama : ")
    umur = int(input("Berapa Umur Kamu? : "))
    asal = input("Asal Kota? :")
    return (nama, umur, asal)


def faktorial(number):
    if number == 0:
        return 1
    else:
        return number * faktorial(number - 1)


def rata_rata(angka):
    hasil = 0
    for i in angka:
        hasil += i
    return hasil/len(angka)


