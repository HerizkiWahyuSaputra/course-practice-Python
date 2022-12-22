print('=====FUNCTION=====') # block of code to be executed if we call the function in code
print('===Non-Paramater Function===')

# Non-paramater Function
# Functions that are not accompanied by parameters in the declaration
def hello_world():
    var = 'Halo Python, hello world!'
    print(var)

hello_world()

print('\n===Paramater Function===')
# Paramater Function
# functions that include parameters in the declaration
def selamat_datang(nama):
    var = f'halo {nama}, welcome!'
    print(var)

selamat_datang('jo')

def selamat_datang(nama, asal):
    var = f'Halo {nama} dari {asal}, welcome!'
    print(var)

selamat_datang('nurul', 'Purwokerto')
selamat_datang(asal='Purwokerto', nama='nurul')

def selamat_datang(*daftar_nama):

    var = 'halo'
    for nama in daftar_nama:
        var += nama + ','

    var += 'welcome!'
    print(var)

selamat_datang('nurul', 'siska', 'lukman', 'mardadi', 'rowi')

print('\n===Anonim Function===')
# Anonim
# function created anonymously using the Lambda keyword
double = lambda x: x * 2

print(double(7))

# Bonus : Docstring

def selamat_datang(nama):
    '''
    ini adalah fungsi untuk menyapa 
    nama yang telah disebutkan
    '''
    var = f'Halo {nama}, welcome!'
    print(var)

selamat_datang('nurul')
print(selamat_datang.__doc__)

# Bonus : scopre & return
a = 2
b= 1

x = 100

def operasi(a,b,c):

    op1 = a+b
    op2 = op1 // c

    print('a di dalam function:', a) 
    print('a di dalam function:', b)

    print(x)

    return op2

hasil = operasi(a=10, b=5, c=3)
print(hasil)

print('a di luar function:', a)
print('a di luar function:', b)
