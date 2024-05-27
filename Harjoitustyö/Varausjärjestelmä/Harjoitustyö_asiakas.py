from Harjoitustyö_funktiot import *

if __name__ == '__main__':
    print("Tervetuloa elokuvateatteriin!")
    next = 0
    while True:
        if next == 0:
            print("Valitse näytös:")
            listaa_naytokset()
            print("0. Poistu")
            print("Enter: Päivitä")

        sali = input("Anna sali: ")

        if sali == "":
            next = 0
            print("")
        else:
            try:
                sali = int(sali)
                next = 1
            except ValueError:
                pause("Anna sali lukumuodossa")
                next = 0

        if next == 1:
            if sali == 0:
                break

            if onko_salissa_naytos(sali) == False:
                pause("Salissa ei ole näytöksiä")
                next = 0
            else:
                try:
                    aika = str(input("Anna aika: "))
                    next = 2
                except ValueError:
                    pause("Anna aika tekstimuodossa")
                    next = 1
                
        if next == 2:
            if onko_naytos(sali, aika) == False:
                pause("Näytöstä ei ole")
                next = 0
            else:
                if onko_salissa_tilaa(sali, aika) == False:
                    pause("Salissa ei ole tilaa")
                    next = 0
                else:
                    try:
                        nimi = str(input("Anna nimesi: "))
                        next = 3
                    except ValueError:
                        pause("Anna nimi tekstimuodossa")
                        next = 2
                if next == 3:
                    lisaa_varaus(nimi, sali, aika)
                    next = 0