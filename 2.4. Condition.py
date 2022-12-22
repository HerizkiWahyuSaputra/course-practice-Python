print('=====CONDITION=====') # Useful benefits of compiling logic programming flows
print('===IF===')
# IF (if true just coding)
# Determine the action to be taken under certain conditions
visit_volume = 13

if visit_volume > 10:
    print("mobil berjalan...")

if visit_volume < 10:
    print("mobil menunggu penumpang lain...")

print("Di luar condition")

print('\n===IF ELSE===')
# IF ELSE (if true or not keep coding)
# determines the actions to be taken according to certain conditions and also determines the actions if the stated conditions are not suitable
score = 78

if score > 75:
    print('lulus')
else : 
    print('Tidak lulus')

print('\n===IF ELIF ELSE===')
# ELIF (Alternative answer for condition)
# used for more than two branching logic
score = 78

if score >=85:
    print('predikat A/Memuaskan')
elif score >= 75:
    print('predikat B/Bagus')
else:
    print('tidak lulus')


# Condition IF in IF
kelas = 3
score = 90

if kelas > 1:

    if score >= 85:
        print('predikat A/Memuaskan')
    elif score >= 75:
        print('predikat B/Bagus')
    else:
        print('Tidak Lulus')

else:

    if score >= 80:
        print('Predikat A/Bagus')
    else:
        print('Tidak Lulus')


# Extract knowledge
num = float(input("masukan angka : "))

if num >= 0:

    if num == 0:
        print("Nol")
    else:
        print("angka positif")