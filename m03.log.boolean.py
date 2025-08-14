#operasi logika atau boolean

#not.or.and.xor

print('======not=====')
a = False
c = not a
print('data a =',c)
print('-------not')
print('data c =',c)

#or
#jika salah satu true maka hasil nya akan true
print('======or=====')
a = False
b = False
c =not a
print(a,'OR',b, '=',c )


a = False
b = True
c =not a
print(a,'OR',b, '=',c )

a = True
b = False
c =not a
print(a,'OR',b, '=',c )

a = True
b = True
c =not a
print(a,'OR',b, '=',c )


#AND (jika dua buah trua maka hasil nya akan true)
print('======AND=====')
a = False
b = False
c =not a
print(a,'AND',b, '=',c )


a = False
b = True
c =not a
print(a,'AND',b, '=',c )

a = True
b = False
c =not a
print(a,'AND',b, '=',c )

a = True
b = True
c =not a
print(a,'AND',b, '=',c )


#XOR(akan true jika salah satu nya true. sisanya false)
print('======XOR=====')
a = False
b = False
c =not a
print(a,'XOR',b, '=',c )


a = False
b = True
c =not a
print(a,'XOR',b, '=',c )

a = True
b = False
c =not a
print(a,'XOR',b, '=',c )

a = True
b = True
c =not a
print(a,'XOR',b, '=',c )

