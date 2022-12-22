print("=====RegEx=====")
# special function to define a certain pattern through a set of characters

import re

print("\n=====MATCH RegEx=====")
teks = "regex"
x = re.match("^r...x$", teks) # mengembalikan status kecocokan
print(x)

print("\n=====SPLIT RegEx=====")
teks = "i'm happy learn regex" 
x = re.split("\s", teks) # mengembalikan list dari string yang telah di split berdasar kecocokan
print(x)

print("\n=====SUB RegEx=====")
teks =  '''
        the 3 loop type in language python programming are while loop,
        for loop and nested loop 2022
        '''
x = re.sub("\d+", "", teks) # mengubah bagian dari string berdasarkan kecocokan
print(x)

print("\n=====SEARCH RegEx=====")
teks = "hujan deras di kawasan depok"
result = re.search("^hujan.*depok$", teks) # mencari kecocokan dimanapun berada yang ada pada string

if result:
    print("YES! we have a match.")
else:
    print("No match.")

print("\n=====FINDALL RegEx=====")
teks = "23 oct 2019 23 oct,2019 23 october,2019 oct 26,2020"
x = re.findall("\d{2} [a-z]{3} \d{4}", teks) # mengembalikan list yang memuat semua string yang cocok
print(x)

print("\n=====SUB RegEx=====")
teks = "Harga 1 mobil antik tersebut yaitu $1000"
x = re.sub("\$\d+", "_", teks) # mengubah bagian dari string berdasarkan kecocokan 
print(x)

print("\n=====SUB RegEx=====")
teks = "Akan dialihkan ke http://medium.com"
x = re.sub("http[s]?\://\S+", "_", teks) # mengubah bagian dari string berdasarkan kecocokan
print(x)

print("\n=====FINDALL RegEx=====")
teks = "Luar biasa! Banyak anak-anak muda traveling tahun ini, begini tanggapan lesti #travel #_lesti #viral #gadget"
x = re.findall("#[_]*[a-z]+", teks) # mengembalikan list yang memuat semua string yang cocok
print(x)
