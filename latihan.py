#LATIHAN MEMBUAT SEBUAH PROGRAM YANG DAPAT MENGKONVERSI SUHU
# 1. DARI CELCIUS KE DERAJAT SUHU YANG LAIN
celcius = float(input("Masukkan suhu dalam celsius : "))
print('Suhu adalah',celcius,'celsius');
reamur = (4/5) * celcius
print('Suhu adalah',reamur,'reamur');
fahrenheit = ((9/5) * celcius) + 32
print('Suhu adalah',fahrenheit,'fahrenheit');
kelvin = celcius + 273
print('Suhu adalah',kelvin,'kelvin');
print('=' * 25)
# 2. DARI FAHRENHEIT KE DERAJAT SUHU YANG LAIN
reamur = float(input('Masukkan suhu dalam reamur : '))
print('Suhu adalah',reamur,'reamur');
celcius = (5/4) * reamur
print('Suhu adalah',celcius,'celsius');
fahrenheit = (9/4) * reamur + 32
print('Suhu adalah',fahrenheit,'fahrenheit');
kelvin = (5/4) * reamur + 273
print('Suhu adalah',kelvin,'kelvin');
print('=' * 25)
# 3. DARI FAHRENHEIT KE DERAJAT SUHU YANG LAIN
fahrenheit = float(input('Masukkan suhu dalam fahrenheit : '))
print('Suhu adalah',fahrenheit,'fahrenheit');
celcius = (5/9) * (fahrenheit - 32)
print('Suhu adalah',celcius,'celsius');
reamur = (4/9) * (fahrenheit - 32);
print('Suhu adalah',reamur,'reamur');
kelvin = celcius + 273
print('Suhu adalah',kelvin,'kelvin');
print('=' * 25);
# 4. DARI KELVIN KE DERAJAT SUHU YANG LAIN
kelvin = float(input('Masukkan suhu dalam kelvin : '))
print('Suhu adalah',kelvin,'kelvin');
celcius = kelvin - 273;
print('Suhu adalah',celcius,'celsius');
reamur = (4/5) * (kelvin - 273)
print('Suhu adalah',reamur,'reamur');
fahrenheit = ((9/5) * celcius) + 32
print('Suhu adalah',fahrenheit,'fahrenheit');