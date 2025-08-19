#episode imput user

#data yang dimasukkan pasti string

data = input("masukan data: ")

print("data = ",data,",type =",type(data))

#jika ingin mengambil data integer maka:

data_int = int(input("masukan angka: "))
print("data = ",data_int,",type =",type(data_int))

##ji   ka ingin mengambil data float maka:
angka = float(input("masukan angka: "))
print("data = ",angka,",type =",type(angka))

#jika ingin mengambil data boolean maka:

biner = bool(int(input("masukan nilai boolean: ")))
print("data = ",biner,",type =",type(biner))