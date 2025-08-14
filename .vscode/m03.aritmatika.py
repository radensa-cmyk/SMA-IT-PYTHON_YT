#operasi aritmatika

# operasi tambahan +

a = 10
b = 3
hasil = a + b

print(a, "+", b, "=", hasil)

#bisa juga dengan F-string (lebih moderen)
a = 10
b = 3
hasil = a + b

print(f"{a} + {b} = {hasil}")



# operasi pengurangan -

a = 10
b = 3
hasil = a - b

print(a, "-", b, "=", hasil)


# operasi perkalian *

a = 10
b = 3
hasil = a * b

print(a, "*", b, "=", hasil)


# operasi pembagian /

a = 10
b = 3
hasil = a / b

print(a, "/", b, "=", hasil)


# operasi exponen (pangkat **)

a = 10
b = 3
hasil = a** b

print(a, "**", b, "=", hasil)

# operasi floor devision //

a = 10
b = 3
hasil = a // b

print(a, "//", b, "=", hasil)


# operasi modulus % (sisa pembagian)

a = 10
b = 3
hasil = a % b

print(a, "%", b, "=", hasil)


#prioritas operasi, operational precedence

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x 
print(x, '**' ,y, '*' ,z, '+' ,x,'/' ,y, '-' ,y, '%' ,z, '//' ,x, '=' ,hasil)
#hasil = 3.7

#1.()
#2.exponen
#3.perkalian dan teman teman %.*.**.//
#4.pertambahan dan pengurangan - +

#jika angka di kurung maka hasil akan berbeda.
#yg dikurung akan di kerjakan dahulu

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x 
print(x, '**' ,y, '*' ,z, '+' ,x,'/' ,y, '-' ,y, '%' ,z, '//' ,x, '=' ,hasil)
#hasil = 31.5