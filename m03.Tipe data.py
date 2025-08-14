# tipe data adalah macam macam data yg bsa di pakain di python
#ada beberapa tipe data
#1 tipe data: angka satuan (integer)
#yg tidak ada koma nya

data_integer = 1

print("data : ", data_integer,)
print("- bertipe : ", type(data_integer))

# data tipe: angka dengan koma (folat)

data_float = 1.5
print("data : ", data_float)
print("- bertipe : ", type(data_float))

# data tipe: kumpulan karakter (string)

data_string = "ucup"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

# data tipe: biner true/false (boolean)

data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))



#tipe data khusus
#bilangan komplexs

data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

#tipe data dari bahasa c

from ctypes import c_double
data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))


