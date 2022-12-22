# Tuple = untuk mengunci data penting agar tidak berubah-ubah (immutable) dengan tanda ( )
print('======TUPLE======')

tuple1 = ("apple", "banana", "watermelon")
tuple2 = (1, 3, 7, 9, 10)
tuple3 = (True, False, False)
tuple4 = ("abc", 10, True, 40, "male")

fruit_taple = ("apple", "banana", "watermelon", "orange", "mango")
# fruit_taple[1]
# fruit_taple[1:4] 
print(fruit_taple[-2:])

# Dictionary = digunakan untuk bentuk data dengan struktur key-value dan berada dalam tanda { }
print('\n======DICTIONARY======')
print('===[key1:value1, key2:value2]===')

fruit_dict = { 'nama'  : 'pisang', #fokus pada key ini yang bisa di panggil
                'jenis' : 'ambon',
                'kode'  : 891, 
                'harga' : 20000,}

print(fruit_dict['jenis'])

fruit_dict['nama'] = 'jeruk'

# print(fruit_dict)

fruit_dict['harga'] = 25000

# print(fruit_dict)

for key, value in fruit_dict.items():
    print(key,value)

for key in fruit_dict.keys():
    print(key,fruit_dict[key])

# BONUS: set (digunakan untuk data seperti himpunan)
print('\n======BONUS======')
print('===SET===')

A = { 1, 2, 3, 4, 5}
B = { 4, 5, 6, 7, 8}

# Union (semua data di ambil sedangkan yang berbeda)
print(A | B)

# intersection (data yang di ambil memiliki data yang sama)
print(A & B)

# Difference (perbedaan dengan objek yang di kurangi)
print(A - B)
print(B - A)

# Symetric Difference (yang di ambil yang difference)
print(A ^ B)