import math


print("Menghitung Luas Persegi Panjang")

P = float(input("Masukan panjang :"))
L = float(input("Masukan lebar :"))
luas = P * L
print("Luas persegi panjang : ", luas)

print("Menghitung luas lingkaran")

r = float(input("Masukan jari-jari :"))
luas_lingkaran = 3.14 * (r ** 2)
print("luas lingkaran : ", luas_lingkaran)

print("#Menghitung Luas kubus")
s = float(input("Masukan panjang sisi :"))
luas_kubus = 6 * (s ** 2)
print("luas kubus :", luas_kubus)

print("#Menghitung Konversi suhu celcius ke Farenheit")

C = float(input("Masukan suhu celcius :"))
F = (C * 9/5) + 32
print("konversi celcius ke farenheit : ", F)

print("Menghitung Konversi Reamur ke Kelvin")
R = float(input("Masukan suhu Reamur :"))
K = (R * 5/4) + 273
print("Konversi Reamur k Kelvin : ", K)



