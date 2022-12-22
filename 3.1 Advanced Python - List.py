print('======LIST======')
# List
# daftar nilai yang dipisahkan tanda koma , antara nilai dan berada dalam tanda [ ]
# bersifat mutable (data dapat di ubah)

list1 = ["apple", "banana", "watermelon"]
list2 = [2, 1, 2, 7, 4, 10]
list3 = [True, False, False]
list4 = ["abc", 10, True, 40, "male"]

list5 = [list4, list3, list2, list1]

# print(list5)

print(list1 + list2) # menjumlahkan dua list

list2.sort() # cara lain ngambil data

print(list2)

# list1.sort()

# print(list1)

list2.reverse() # urutannya di balik

print(list2)

list3 = list2.copy()

print(list3.count(2))

fruit_list = ['apple', 'banana', 'watermelon', 'orange', 'mango']
# print(fruit_list[1])
# print(fruit_list[1:5])
# print(fruit_list[-3])
print(fruit_list[-3:])

fruit_list[2] = "avocado"
print(fruit_list)

print('\n====Member List====')
# Membership list (untuk menambah data)

print('apple' in fruit_list)
print('apple' not in fruit_list)

fruit_list = ['apple', 'banana',]
fruit_list.append("watermelon")

print(fruit_list)

fruit_list.insert(1, "orange")

print(fruit_list)

fruit_list1 = ['apple', 'banana',]
fruit_list2 = ['apple', 'watermelon',]

fruit_list1.extend(fruit_list2)

print(fruit_list1)


print('\n====List untuk Remove====')
# Remove (untuk menghapus data)

fruit_list = ['apple', 'orange', 'banana', 'watermelon'] # cara 1 delete
fruit_list.remove("orange")

print(fruit_list)

fruit_list = ['apple', 'orange', 'banana', 'watermelon'] # cara 2 delete
fruit_list.pop(2)

print(fruit_list)

fruit_list = ['apple', 'orange', 'banana', 'watermelon'] # cara 3 delete
del fruit_list[1]

print(fruit_list)

fruit_list.clear()

print(fruit_list)