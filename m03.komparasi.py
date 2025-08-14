#operasi komparasi
 # setiap hasil dari operasi komparasi adalah boolean

# >,<,>=,<=,==,is,is not

a = 4
b = 2

# lebih besar dari >
print('======lebih besar dari (>)')
hasil = a > 3
print(a, '>' ,3, '=' ,hasil) 
#hasil true.mengapa hasi bisa true?
#karena jumalh a lebih besar dari angka 3

hasil = b > 3
print(b, '>' ,3, '=' ,hasil)
#hasil false. mengapa?,
#karena jumlah b lebih kecil dari angka 3

hasil = b > 2
print(b, '>' ,2, '=' ,hasil)
#hasil false, why? karena jika angka ingin sama maka 
#angka 2 harus di tambahka 2.1



#lebih kecil dari <
print('======lebih kecil dari (<)')
hasil = a < 3
print(a, '<' ,3, '=' ,hasil)

hasil = b < 3
print(b, '<' ,3, '=' ,hasil)


hasil = b < 2
print(b, '<' ,2, '=' ,hasil)



#lebih dari sama dengan >=
print('======lebih dari sama dengan (>=)')
hasil = a >= 3
print(a, '>=' ,3, '=' ,hasil)

hasil = b >= 3
print(b, '>=' ,3, '=' ,hasil)


hasil = b >= 2
print(b, '>=' ,2, '=' ,hasil)



#kurang dari sama dengan <=
print('======kurang dari sama dengan (>=)')
hasil = a <= 3
print(a, '<=' ,3, '=' ,hasil)

hasil = b <= 3
print(b, '<=' ,3, '=' ,hasil)


lprint(b, '<=' ,2, '=' ,hasil)


# sama dengan ==
print('===== sama dengan (==)')
hasil = a == 4
print(a, '==', 4, '=', hasil)
# == artinya perbandingan, memastikan apakah nilai
# a = 4 jika benar maka ia akan true jiak salah maka akan false


# tidak sama dengan !=
print('===== tidak sama dengan (!=)')
hasil = a != 4
print(a, '!=', 4, '=', hasil)
#kebalikan nya



#is sebagai operasi objeck identity
# Identik (is)
print('===== objec identity (is)')
hasil = a is b
print(f"{a} is {b} = {hasil}")
# membandingkan objec,
#jika kode nya a is 4 maka tidak akan jalan
#jika kode nya a is b maka akan jalan


# Tidak identik (is not)
hasil = a is not b
print(f"{a} is not {b} = {hasil}")