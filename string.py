

data = "ini adalah string"
print(data)
print(type(data))


#cara membuat string

# 1 dengan menggunakan single quote '...'
# 2 dengan menggunakn dubble quote  "..."
# menggabungkan 22 nya

data = 'menggunakan single quate'
print(data)

data = "menggunakan dubble quote"
print(data)

data = '"menggunakan 22 nya"'
print(data)

# 2 menggunakan tanda\
#cara membuat tanda ' menjadi str

#print('mari shalat jum'at') jiika seperti ini maka false karena ada koma 3

print('mari shalat jum\'at')
#harus ada tanda \ supaya bisa di tutup '

#backslas
print('\\user\\RADENSA')

# tab
print("ucup \totong")
# tulisan menjauh \t

#back space
print("ucup \botong")
# mendekat \b


# newline
print("baris pertama.\nbaris kedua.") # lf -> linefeed -> unic,macos, linux
print("baris pertama.\rbaris kedua.")# cr -> carriage return -> acorn.
print("baris perytama.\r\nbaris kedua.") #crlf line feed carriage -> windows

#string literal
raw_text = r"Baris pertama\nBaris kedua"
print(raw_text)

teks = """Ini adalah baris pertama.
Ini adalah baris kedua.
Dan ini adalah baris ketiga."""
print(teks)
