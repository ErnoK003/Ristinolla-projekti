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

def tulosta_peli(yks, kaks, kolme, nelja, viis, kuus, seittema, kaheksa, yheksa):
    print(yks, kaks, kolme)
    print(nelja, viis, kuus)
    print(seittema, kaheksa, yheksa)

def paikka(valinta, merkki, yks, kaks, kolme, nelja, viis, kuus, seittema, kaheksa, yheksa):

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

def voittiko(lista):
    voittolista1=[1,2,3]
    voittolista2=[4,5,6]
    voittolista3=[7,8,9]
    voittolista4=[1,4,7]
    voittolista5=[2,5,8]
    voittolista6=[3,6,9]
    voittolista7=[1,5,9]
    voittolista8=[3,5,7]
    if sorted(lista) == voittolista1 or sorted(lista) == voittolista2 or sorted(lista) == voittolista3 or sorted(lista) == voittolista4 or sorted(lista) == voittolista5 or sorted(lista) == voittolista6 or sorted(lista) == voittolista7 or sorted(lista) == voittolista8:
        return True
    return False


print("Tervetuloa ristinolla-peliin!")
pelipaal = 1
vuoro = 1
vuoromaara = 1

while pelipaal == 1:
    tulosta_peli(yks, kaks, kolme, nelja, viis, kuus, seittema, kaheksa, yheksa)


    if vuoro == 1:
        valinta = int(input("Pelaaja 1 vuoro. Valitse paikka - olet X (1-9): "))
        xlista.append(valinta)
        yks, kaks, kolme, nelja, viis, kuus, seittema, kaheksa, yheksa, onnistui = paikka(valinta, "X", yks, kaks, kolme, nelja, viis, kuus, seittema, kaheksa, yheksa)

        if onnistui:
            vuoromaara+=1
            vuoro = 2
            if voittiko(xlista)==True:
                tulosta_peli(yks, kaks, kolme, nelja, viis, kuus, seittema, kaheksa, yheksa)
                print("Pelaaja 1 voitti!")
                break
            elif vuoromaara==10:
                vuoro=0
    elif vuoro == 2:
        valinta = int(input("Pelaaja 2 vuoro. Valitse paikka - olet O (1-9): "))
        olista.append(valinta)
        yks, kaks, kolme, nelja, viis, kuus, seittema, kaheksa, yheksa, onnistui = paikka(valinta, "O", yks, kaks, kolme, nelja, viis, kuus, seittema, kaheksa, yheksa)

        if onnistui:
            vuoromaara+=1
            vuoro = 1
            if voittiko(olista)==True:
                tulosta_peli(yks, kaks, kolme, nelja, viis, kuus, seittema, kaheksa, yheksa)
                print("Pelaaja 2 voitti!")
                break
            elif vuoromaara==10:
                vuoro=0
    
    else:
        print("Tasapeli.")
        break