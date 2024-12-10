def tulosta_peli(yks, kaks, kolme, nelja, viis, kuus, seittema, kaheksa, yheksa):      #tulostaa pelilaudan
    print(yks, kaks, kolme)
    print(nelja, viis, kuus)
    print(seittema, kaheksa, yheksa)

def paikka(valinta, merkki, yks, kaks, kolme, nelja, viis, kuus, seittema, kaheksa, yheksa):
                            #asettaa halutulle paikalle pelaajan merkin, jos paikka on vapaa ja kysyy niin kauan, kunnes onnistuu (True)
    if valinta == 1 and yks == "1":
        yks = merkki
    elif valinta == 2 and kaks == "2":
        kaks = merkki
    elif valinta == 3 and kolme == "3":
        kolme = merkki
    elif valinta == 4 and nelja == "4":
        nelja = merkki
    elif valinta == 5 and viis == "5":
        viis = merkki
    elif valinta == 6 and kuus == "6":
        kuus = merkki
    elif valinta == 7 and seittema == "7":
        seittema = merkki
    elif valinta == 8 and kaheksa == "8":
        kaheksa = merkki
    elif valinta == 9 and yheksa == "9":
        yheksa = merkki
    else:
        print("Paikka on jo varattu! Valitse toinen paikka.")
        return yks, kaks, kolme, nelja, viis, kuus, seittema, kaheksa, yheksa, False
    return yks, kaks, kolme, nelja, viis, kuus, seittema, kaheksa, yheksa, True 

def voittiko(lista):                #tarkastaa voittiko juuri asettanut pelaaja
    voittolista1=[1,2,3]
    voittolista2=[4,5,6]
    voittolista3=[7,8,9]
    voittolista4=[1,4,7]
    voittolista5=[2,5,8]
    voittolista6=[3,6,9]
    voittolista7=[1,5,9]
    voittolista8=[3,5,7]
    if set(voittolista1).issubset(set(lista)) or set(voittolista2).issubset(set(lista)) or set(voittolista3).issubset(set(lista)) or set(voittolista4).issubset(set(lista)) or set(voittolista5).issubset(set(lista)) or set(voittolista6).issubset(set(lista)) or set(voittolista7).issubset(set(lista)) or set(voittolista8).issubset(set(lista)):
        return True
    return False
yks="1"
kaks="2"
kolme="3"
nelja="4"
viis="5"
kuus="6"
seittema="7"
kaheksa="8"
yheksa="9"
xlista=[]
olista=[]
pelipaal = 1
vuoro = 1
vuoromaara = 1
print("Tervetuloa ristinolla-peliin!")

while pelipaal == 1:                #pääohjelma, peli pysyy käynnissä, kunnes joku voittaa tai tulee tasapeli
    tulosta_peli(yks, kaks, kolme, nelja, viis, kuus, seittema, kaheksa, yheksa)


    if vuoro == 1:             #x:n vuoro
        valinta = int(input("Pelaaja 1 vuoro. Valitse paikka - olet X (1-9): "))
        xlista.append(valinta)
        yks, kaks, kolme, nelja, viis, kuus, seittema, kaheksa, yheksa, onnistui = paikka(valinta, "X", yks, kaks, kolme, nelja, viis, kuus, seittema, kaheksa, yheksa)

        if onnistui:            #jos asettaminen onnistui, tarkastetaan voittiko, jos ei, niin toisen pelaajan vuoro
            vuoromaara+=1
            vuoro = 2
            if voittiko(xlista)==True:
                tulosta_peli(yks, kaks, kolme, nelja, viis, kuus, seittema, kaheksa, yheksa)
                print("Pelaaja 1 voitti!")
                break
            elif vuoromaara==10:
                vuoro=0
    elif vuoro == 2:               #O:n vuoro
        valinta = int(input("Pelaaja 2 vuoro. Valitse paikka - olet O (1-9): "))
        olista.append(valinta)
        yks, kaks, kolme, nelja, viis, kuus, seittema, kaheksa, yheksa, onnistui = paikka(valinta, "O", yks, kaks, kolme, nelja, viis, kuus, seittema, kaheksa, yheksa)

        if onnistui:             #jos asettaminen onnistui, tarkastetaan voittiko, jos ei, niin toisen pelaajan vuoro
            vuoromaara+=1
            vuoro = 1
            if voittiko(olista)==True:
                tulosta_peli(yks, kaks, kolme, nelja, viis, kuus, seittema, kaheksa, yheksa)
                print("Pelaaja 2 voitti!")
                break
            elif vuoromaara==10:
                vuoro=0
    
    else:                         #elseen päästään vain, jos kumpikaan ei voi enää asettaa ja peli päättyy
        print("Tasapeli.")
        break