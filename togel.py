#!/usr/bin/python
#coder : putri sitasari
#cewek cantik calon presiden
#togel decrypter
#buat acak angka index
#sifatnya kalau udah muncul di bagi dengan angka pasti
#kalau angka pasti dari bandar nggak cocok
#ya main lagi,namanya buat acak

import random

index = 4
ask = [raw_input('masukkan prediksi angka index ') for x in range(index)]

for x in range(52):
    a = range(1,100)

    people = {}
    for i in ask:
        randomnum = random.choice(a)
        a.remove(randomnum)  ## tahan masukkan dua angka yang sama
        people[i] = randomnum
    
    ##realnum = random.randint(1,100)         ## kalau ada yang masukkan dua angka
    realnum = random.choice(people.values())  ## kalau ada yang menang randomize lagi(default)


    ## Check -- ada yang menang?


    for x,y in people.items():
        if y == realnum:
            print "%s eh mungkin strike angkanya" % x
    raw_input("kalau kurang yakin coba lagi lah ")