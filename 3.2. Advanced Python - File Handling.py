
print('\n======File Handling======') # special function to manage files
print('===READ===')
# Read
# for read file

# data = open('./data.txt', mode='r')
# print(data.read(5))
# print(data.read())

data = open('./data.txt', mode='r', encoding='utf-8') # recommended
print(data.read())

string = data.read()
string = string.replace('adalah', 'merupakan')
print(string)
 

print('\n====APPEND====')
# Append
# for add data

data = open('./data.txt', mode='a', encoding='utf-8') # recommended
data.write("\nYuk belajar bahasa pemgrograman Python!")

data.close()

print('\n====WRITE====')
# Write
# for write data

data = open('./data.txt', mode='w', encoding='utf-8') # recommended
data.write("\nYuk belajar bahasa pemgrograman Python")
data.write("\nSering Latihan supaya Jago")

data.close()


# Better Practice
print('\n====BETTER PRATICE====')
# try:
    # f = open('./data.txt', mode='w', encoding='utf-8')
# finally:
    # f.close()

# Best Practice (yang sebaiknya digunakan saat melakukan File Handling)
print('\n====BEST PRACTICE====')
# with open('./data.txt', mode='w', encoding='utf-8') as f:
    # bisa diisi code apa saja
    # f.read()
    # f.write()
    # f.write()
    # pass