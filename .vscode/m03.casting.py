#merubah satu data ke tipe data yg lain

#data integer
print("====integer====")
data_int = 9;
print("data = ", data_int, "type =",type(data_int))


data_float = float(data_int)
print("data = ", data_float, "type =",type(data_float))



data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data = ", data_float, "type =",type(data_float))
print("data = ", data_str, "type =",type(data_str))
print("data = ", data_bool, "type =",type(data_bool))


#data float

print("====float====")
data_bool = 9.5;
print("data = ", data_float, "type =",type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
print("data = ", data_int, "type =",type(data_int))
print("data = ", data_str, "type =",type(data_str))
print("data = ", data_bool, "type =",type(data_bool))




#data boolean

print("====boolean====")
data_bool = True;
print("data = ", data_bool, "type =",type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_bool = float(data_bool)
print("data = ", data_int, "type =",type(data_int))
print("data = ", data_str, "type =",type(data_str))
print("data = ", data_float, "type =",type(data_float))


#data string

print("====string====")
data_str = 0;
print("data = ", data_str, "type =",type(data_str))

data_int    = int(data_str)#akan dibulatkan ke bawah
data_float    = str(data_str)#akan false jika nilai float
data_boll   = float(data_str)
print("data = ", data_int, "type =",type(data_int))
print("data = ", data_float, "type =",type(data_float))
print("data = ", data_boll, "type =",type(data_bool))

#string harus angka


