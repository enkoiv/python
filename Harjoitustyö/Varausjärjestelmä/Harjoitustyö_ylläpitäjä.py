from Harjoitustyö_funktiot import *

#next-muuttuja antaa paikan, johon palataan loopissa
next = -1
if __name__ == '__main__':
    print("Tervetuloa!")
    while True:
        if next == -1:
            print("Valitse:")
            print("1. Lisää näytös")
            print("2. Lisää elokuva")
            print("3. Selaa tietokantaa")
            print("4. Tyhjennä tietokanta")
            print("0. Poistu")

            try:
                choice = int(input("Valinta: "))
                next = 0
            except ValueError:
                pause("Anna valinta lukumuodossa")
                next = -1

        if next == 0:
            if choice == 0:
                break

            if choice == 1:
                listaa_salit()
                try:
                    hall = int(input("Anna sali: "))
                    next = 1
                except ValueError:
                    pause("Anna sali lukumuodossa")
                    next = 0

            choices = [0, 1, 2, 3, 4]
            if choice not in choices:
                pause("Ei kelvollinen valinta")
                choice = -1
                next = -1

        if next == 1:
            if onko_sali(hall) == False:
                next = 0
                pause("Salia ei löytynyt")
            else:
                time = str(input("Anna aika: "))
            
                success = True
                for i in time:
                    if i not in "0123456789.":
                        success = False
                
                if success == False:
                    print("Ajassa voi olla numeroita ja piste")
                    next = 1
                else:
                    next = 2

        if next == 2:
            if onko_naytos(hall, time) == False:
                movie = str(input("Anna elokuva: "))
                next = 3
            else:
                pause("Salissa on jo näytös tuohon aikaan")
                choice = -1
                next = -1

        if next == 3:
            if onko_elokuva(movie) == False:
                pause("Elokuvaa ei ole")
            else:
                lisaa_naytos(hall, time, movie)
            next = -1
            choice = -1

        if choice == 2:
            next = -1
            choice = -1

            movie = str(input("Anna elokuva: "))
            
            if movie == "":
                pause("Elokuvan nimi ei voi olla tyhjä")
            else:
                if onko_elokuva(movie) == True:
                    pause("Elokuva on jo lisätty")
                else:
                    lisaa_elokuva(movie)


        if choice == 3:
            next = -1
            choice = -1
            print("")
            print("Valitse:")
            print("1. Salit")
            print("2. Elokuvat")
            print("3. Näytökset")
            print("4. Varaukset")
            choice2 = int(input("Valinta: "))

            if choice2 == 1:
                listaa_salit()
                pause2()
            elif choice2 == 2:
                if listaa_elokuvat() == "empty":
                    print("Ei elokuvia")
                pause2()
            elif choice2 == 3:
                listaa_naytokset()
                pause2()
            elif choice2 == 4:
                selaa_varauksia()
                pause2()

        if choice == 4:
            next = -1
            choice = -1
            print("Tämä tyhjentää elokuvat, näytökset ja varaukset")
            choice2 = input("Jos olet varma, kirjoita k: ")
            if choice2 == "k":
                pause("Tyhjennetty")
                luo_tietokanta()
            else:
                pause("Peruutettu")

