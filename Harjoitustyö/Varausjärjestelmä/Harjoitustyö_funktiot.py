#Tekstitiedoston polku:
import os, sys
tiedosto = os.path.join(sys.path[0], "Tekstit.txt")

def listaa_tiedostosta(aloitus: str, lopetus: str) -> list:
    with open(tiedosto, encoding="utf-8") as file:
        rows = file.readlines()

        #luo lista riveistä välillä ]aloitus,lopetus[
        lista = []
        lue = False
        for row in rows:
            row_strip = row.strip("\n")
            if lue == True:
                if row_strip == lopetus:
                    lue = False
                else:
                    lista.append(row_strip)
            if row_strip == aloitus:
                lue = True

        #jaa tiedot ja luo listat niistä riveittäin
        lista2 = []
        for i in range(len(lista)-1):
            rivi = lista[i]
            rivi2 = rivi.split(",")
            lista2.append(rivi2)

        return lista2

def kirjoita_tiedostoon(tieto: str, aloitus: str, lopetus: str):
    with open(tiedosto, encoding="utf-8") as file:
        rows = file.readlines()

        lue_tiedot = False
        i = 0
        empty_row = False
        #etsitään tyhjä rivi syötteen kirjoittamista varten
        for row in rows:
            row_strip = row.strip("\n")
            
            #lopettaa for-loopin, kun lukee "<lopetus>"
            if lue_tiedot == True:
                if row_strip == lopetus:
                    lue_tiedot = False
                #tarkistaa, onko rivi tyhjä
                else:
                    if empty_row == False:
                        if row_strip == "":
                            empty_row = True
                            j = i
            
            #etsii "<aloitus>", josta aloittaa
            if row_strip == aloitus:
                lue_tiedot = True
            i += 1

        #vaihtaa rivin syötteeksi
        try:
            rows[j] = tieto + "\n" + "\n"
        except IndexError:
            rows[-1] = tieto + "\n" + "\n"

    #kirjoitetaan tiedostoon UTF-8:lla, jotta esim. ääkköset säilyvät
    with open(tiedosto, "w", encoding="utf-8") as file:
        content = ""
        for row in rows:
            content += row
        file.write(content)

def listaa_naytokset():
    lista = listaa_tiedostosta("sali, aika, nimi", "varaukset:")

    if lista == []:
        print("Ei näytöksiä")
    else:
        try:
            for i in range(len(lista)):
                lista2 = []
                if lista[i] == ['']:
                    pass
                else:
                    for j in lista[i]:
                        lista2.append(j)
                    print(f"Sali: {lista2[0]} Aika: {lista2[1]} Nimi: {lista2[2]}")
        except IndexError:
            print("Ei näytöksiä")


def onko_salissa_naytos(sali: int) -> bool:
    lista = listaa_tiedostosta("sali, aika, nimi", "varaukset:")
    
    success = False
    for i in range(len(lista)):
        lista2 = []
        for j in lista[i]:
            lista2.append(j)
        if lista2[0] != "":
            if int(lista2[0]) == sali:
                success = True
    
    if success == True:
        return True
    else:
        return False

def onko_naytos(sali: int, aika: str) -> bool:
    lista = listaa_tiedostosta("sali, aika, nimi", "varaukset:")
    
    success = False
    for i in range(len(lista)):
        lista2 = []
        for j in lista[i]:
            lista2.append(j)
        if lista2[0] != "":
            if (int(lista2[0]) == sali) and (lista2[1] == aika):
                success = True
    
    if success == True:
        return True
    else:
        return False

def lue_varaukset() -> dict:
    rows = listaa_tiedostosta("nimi, sali, aika", "loppu")
    
    varaukset = {}
    try:
        for row in rows:
            varaukset[row[0]] = (row[1],row[2])
    except IndexError:
        pass

    return varaukset

def lisaa_varaus(nimi: str, sali: int, aika: str):
    varaukset = lue_varaukset()
    
    success = True
    #onko jo sama varaus
    for key in varaukset:
        if key == nimi:
            success = False
            pause("Nimelläsi on jo varaus")
    
    if success == True:
        varaukset[nimi] = (sali,aika)
        tuple = f"{nimi},{sali},{aika}"
        kirjoita_tiedostoon(tuple, "nimi, sali, aika", "loppu")
        pause("Lisätty")

def pause(sana: str):
    print(f"{sana}.")
    pause = input("Paina Enter jatkaaksesi...")
    print("")

def pause2():
    pause = input("Paina Enter jatkaaksesi...")
    print("")

def listaa_salit():
    lista = listaa_tiedostosta("numero, koko", "elokuvat:")

    for i in range(len(lista)):
        print(f"Sali {lista[i][0]}, koko {lista[i][1]}")

def lisaa_sali(numero: int, koko: int):
    kirjoita_tiedostoon(f"{numero},{koko}","numero, koko","elokuvat:")
    pause("Lisätty")

def lisaa_naytos(sali: int, aika: str, elokuva: str):
    tieto = f"{sali},{aika},{elokuva}"
    kirjoita_tiedostoon(tieto, "sali, aika, nimi", "varaukset:")
    pause("Lisätty")

def lisaa_elokuva(nimi: str):
    kirjoita_tiedostoon(nimi, "nimi", "näytökset:")
    pause("Lisätty")

def selaa_varauksia():
    varaukset = lue_varaukset()
    
    if varaukset == {}:
        print("Ei varauksia")

    for key in varaukset:
        print(f"Nimi: {key} Sali: {varaukset[key][0]} Aika: {varaukset[key][1]}")

def onko_salissa_tilaa(sali: int, aika: str) -> bool:
    varaukset = lue_varaukset()

    #lasketaan varausten määrä
    counter = 0
    tuple2 = (str(sali), str(aika))
    for key in varaukset:
        if varaukset[key] == tuple2:
            counter += 1
    
    #etsitään salin koko
    lista = listaa_tiedostosta("numero, koko", "elokuvat:")

    for i in range(len(lista)):
        if int(lista[i][0]) == sali:
            size = int(lista[i][1])

    if counter < size:
        return True
    else:
        return False

def onko_elokuva(nimi: str) -> bool:
    lista = listaa_tiedostosta("nimi", "näytökset:")

    success = False
    for i in lista:
        if nimi == i[0]:
            success = True
    
    return success

def onko_sali(sali: int) -> bool:
    lista = listaa_tiedostosta("numero, koko", "elokuvat:")

    success = False
    for i in lista:
        if int(i[0]) == sali:
            success = True
    
    return success

def listaa_elokuvat():
    lista = listaa_tiedostosta("nimi", "näytökset:")
    
    if lista == []:
        return "empty"
    else:
        for i in range(len(lista)):
            for i in lista[i]:
                print(f"Nimi: {str(i)}")

def luo_tietokanta():
    with open(tiedosto, "r", encoding="utf-8") as file:
        rows = []
        rows.append("salit:\n")
        rows.append("numero, koko\n")
        
        salit = listaa_tiedostosta("numero, koko", "elokuvat:")
        
        lista = [salit[i] for i in range(len(salit))]
        lista2 = [",".join(i) for i in lista]

        for i in lista2:
            rows.append(i+"\n")
        rows.append("\n")

        rows.append("elokuvat:\n")
        rows.append("nimi\n")
        rows.append("\n")
        rows.append("näytökset:\n")
        rows.append("sali, aika, nimi\n")
        rows.append("\n")
        rows.append("varaukset:\n")
        rows.append("nimi, sali, aika\n")
        rows.append("\n")
        rows.append("loppu")

        content = ""
        for i in rows:
            content += i
        
    with open(tiedosto, "w", encoding="utf-8") as file:
        file.write(content)