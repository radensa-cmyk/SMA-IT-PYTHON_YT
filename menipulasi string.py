#menyambung string contatenate

nama_pertama = "ucup"
nama_tengah = "d"
nama_akhir = "fame"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2 mengjitung nama string
panjang = len(nama_lengkap)
print(panjang)

#mengecek nama komponen

d = "d"

status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

d = "d"

status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

d = "d"

status = d not in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

#mengulang string
print("wk"*10)
print(15*"wk")

#indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-6 : " + nama_lengkap[6])