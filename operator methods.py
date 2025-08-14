#operator dalam bentuk methods

##merubah case dari string
#merubah semua ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

#merubah semua ke lower case

alay = "aku kece abizz"
print("normal = " + alay) 
alay = alay.lower()
print("lower = " + alay)

#pengecekan dengan isx method

#contoh pengecekan olwer case

# Contoh string
a = "python"
b = "Python"
c = "python123"
d = "python!"
e = "12345"
f = "python world"
g = ""  # string kosong

# Pengecekan
print(a.islower())  # True → semua huruf kecil
print(b.islower())  # False → ada huruf kapital 'P'
print(c.islower())  # True → huruf semua kecil, angka diabaikan
print(d.islower())  # True → huruf semua kecil, simbol diabaikan
print(e.islower())  # False → tidak ada huruf sama sekali
print(f.islower())  # True → semua huruf kecil (termasuk spasi)
print(g.islower())  # False → string kosong

#isalpha () untik mengecek semua huruf
#isalnum() huruf dan angka
#isdecimal() angka saja
#isspace()spasi,tab,newline

#istitle() semua kata dimulai dengan huruf besar

judul = "The Lion King"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))