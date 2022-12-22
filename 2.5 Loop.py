print('=====LOOP=====') # a method of repeatedly executing a program for the purpose of short the code
print('===WHILE LOOP===')
# While Loop
# A statement can be loop executed as long as the condition evaluates to true
count = 0

while (count < 9):
    print("Nilai count:", count)
    count = count + 1

print("selamat berjuang!")

print('\n===FOR LOOP===')
# For Loop
# the ability to repeat items from a sequence such as a list or string
list_angka = [1,2,3,4,5]

for x in list_angka:
    print("intruksi berjalan...")
    print(x)

print(range(10)) # ini berguna untuk digunakan ketika angka sampai puluhan & ribuan.

list_range = list(range(10))
print(list_range)

for x in list(range(2, 20 , 3)):
    print(x)

for x in list(range(1, 11)):
    print(x)

print('\n===NESTED LOOP===')
# Nested Loop
# Loop in Loop
i = 90

while(i < 100):

    j = 2
    print((i/j))
    while(j <+ (i/j)):
        print("loop dalam loop!")
        j = j + 1
        i = i + 1

print("Selamat Berjuang")

print('\n===BREAK & CONTINUE===')
# Break & Continue
# Break has the meaning of ending the loop process
# continue skipping 1 loop process and continue the next loop
for val in "string":

    if val == "g":
        continue
    
    print(val)


for val in "string":

    if val == "i":
        break
    
    print(val)

print("loop telah berakhir.")

print('\n===FOR ELSE===')
# Add knowledge; Bonus : For Else
daftar_murid = ['Angga', 'Mardadi', 'Rowi']

nama_murid = 'Jaka'

for nama in daftar_murid:

    if nama == nama_murid:
        print((nama))
        break

else:
    print('nama murid tidak ditemukan')

# kondisi terpenuhi
daftar_murid = ['Angga', 'Mardadi', 'Rowi']

nama_murid = 'Angga'

for nama in daftar_murid:

    if nama == nama_murid:
        print((nama))
        break

else:
    print('nama murid tidak ditemukan')

# Add knowledge : Pass (kegunaan untuk next jika menunda pengisian)
for nama in daftar_murid:
    pass

if daftar_murid == 0:
    pass

else:
    pass