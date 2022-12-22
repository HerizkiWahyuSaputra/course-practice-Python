# This is learn practical Variable
print('=====VARIABLE=====')

number = 10 # integer
print(number)

number = 100 # integer
print(number)

number = 0.1 # float
print(number)

email = "contact@gmail.com" # string
print(email)

number1, number2, email = 10, 0.1, "contact@gmail.com" # integer, float, string
print(number1)
print(number2)
print(email)

number1 = number2 = number3 = 100 # like because equal between variable for integer
print(number1)
print(number2)
print(number3)

# CONSTANTA VARIABLE (number not change)
PI = 3.14
GRAVITY = 9.8

# Naming
variable_name = "indonesia AI 1" # string
VARIABLE_NAME = "Indonesia AI 2" # attention for charachters

#prohibited : !, @, #, $, % digit 0-9 at early variable

# literals
biner_number = 0b1010 
decimal_number = 100
float_number = 1.5e2

print(float_number)

# This is Learn Practical Data Type
print('\n=====DATA TYPE=====')

a = 5 # integer
print(type(a))

b = 3.0 # float
print(type(b))

c = 4/5 # float
print(type(c))

c = a + b # float
print(type(c))

a = float(a) # float
print(type(a))

c = int(4/5) # integer
print(type(c))
print(c)

a = str(a) # integer
print(a)

print('\n=====DIFFERENT METHOD=====')

c = 8/5 
c = c.__ceil__() # rounded up
print(c)

c = 8/5
c = c.__float__() # permanent
print(c)

print('\n=====STRING=====')

s = "this is single-line string" # string
print(type(s))

s='''this is string
but not single line, this multi-line 
'''
print(type(s))  # string

s = "This is Single-Line String"
s = s.lower() # change capitalization
print(s)

s = "This is Single-Line String"
s = s.upper() # change capitalization
print(s)

s = "This is Single-Line String"
s = s.replace('is', 'of' ) # change characters
print(s)

name = "Riz"
s = f"my name is {name}" # string
print(s)

print('\n=====BINARY TYPE=====')
#Boolean
# True and True = True
# False and True = False
b = True # Boolean
print(type(b))
print(type(b ==1))

print(b == 1)
print(b == 0)

print(False and True)
print(False or True)

print('\n=====SEQUENCE TYPE=====')
print('=====List, Tuple and Dictionary=====')

# List, Tuple and Dictionary
l = [1, 2.2, 'python'] # List
print(type(l))

t = (5, 'program', 1+3) # Tuple
print(type(t))

d = {'key':'value', 'key2':'value'} # Dictionary
print(type(d))
