#operator bitwise,operasi binar/binary
#bitwise = operasi masing masing bit

a = 9
b = 5

#bitwise or (|)
c = a | b
print('=====or=====')
print('nilai : ', a, ', binary : ', format(a, '08b'))
print('nilai :', b, ', binary :', format(b, '08b'))
print('-----------------|')
print('nilai :', c, ', binary :', format(c, '08b'))

#bitwise and (&)
c =a & b
print('=====AND=====')

print('nilai : ', a, ', binary : ', format(a, '08b'))
print('nilai :', b, ', binary :', format(b, '08b'))
print('-----------------&')
print('nilai :', c, ', binary :', format(c, '08b'))


#bitwise XOR  (^)
c =a ^ b
print('=====XOR=====')

print('nilai : ', a, ', binary : ', format(a, '08b'))
print('nilai :', b, ', binary :', format(b, '08b'))
print('-----------------^')
print('nilai :', c, ', binary :', format(c, '08b'))


#bitwise not  (~)
c =a ^ b
print('=====NOT=====')
a = 9               # Biner: 00001001
c = ~a              # Bitwise NOT

print("a       =", a, ", binary:", format(a, '08b'))
print("~a      =", c, ", binary:", format(c & 0xFF, '08b'))  # masking 8 bit

d = 0B0000001001
e = 0B1111111111
# Definisi nilai dalam biner
d = 0b0000001001  # 9
e = 0b11111111    # 255

# Operasi XOR (bitwise exclusive or)
hasil = e ^ d

# Menampilkan hasil
print('nilai :', hasil, ', binary :', format(hasil, '08b'))


#  1. Left Shift (<<)
# Menggeser bit ke kiri, artinya setiap geseran ke kiri berarti dikalikan dengan 2.

a = 5  # biner: 00000101
b = a << 1
print("a =", a, ", binary:", format(a, '08b'))
print("a << 1 =", b, ", binary:", format(b, '08b'))
# O
# a = 5 , binary: 00000101  
# a << 1 = 10 , binary: 00001010
# Karena 5 * 2 = 10

# 2. Right Shift (>>)
# Menggeser bit ke kanan, artinya setiap geseran ke kanan berarti dibagi 2 (tanpa koma, dibulatkan ke bawah).

a = 20  # biner: 00010100
b = a >> 2
print("a =", a, ", binary:", format(a, '08b'))
print("a >> 2 =", b, ", binary:", format(b, '08b'))
