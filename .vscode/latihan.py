#latihan konversi satuan temperature    

#progrsm konversi celcius ke satuan lain

print("/nPROGRAM KONVERSI TEMPERATUR\n")
 
celcius = float(input('masukan suhu dalam celcius : '))
print("suhu adalah",celcius,"celcius")  

#reamur
#rumus = 4/5*c

reamur = (4/5) * celcius
print("suhu dalam reamur adalah",reamur,"reamur")

#fahrenheit
#rumus = 9/5 * celcius + 32

# Konversi ke Fahrenheit
fahrenheit = (9/5) * celcius + 32
print("suhu dalam fahrenheit adalah", fahrenheit, "fahrenheit")

#kelvin
kelvin = celcius + 273.15
print("suhu dalam kelvin adalah", kelvin, "kelvin")


#tugass

#rumus fahrenheit ke kelvin
fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
kelvin = (5/9) * (fahrenheit - 32) + 273.15
print("Suhu dalam Kelvin adalah:", kelvin, "K")


#rumus kelvin ke vahrenheit

kelvin = float(input("Masukkan suhu dalam Kelvin: "))
fahrenheit = (9/5) * (kelvin - 273.15) + 32
print("Suhu dalam Fahrenheit adalah:", fahrenheit, "°F")

