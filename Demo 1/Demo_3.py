first = True
is_list = 0
list = ""

while True:
    command = input("Anna tunnus/komento: ")
    
    if command == "lopeta":
        break
    elif command == "lista":
        print(list)

    #muokataan tunnus muotoon ppkkvvnnn
    if command != "lista" and command != "":
        checking_number = f"{command[0:6]}{command[7:10]}"
        #lasketaan tarkistustunnuskaavalla jakojäännös
        checking_code = int(checking_number) % 31
        #tarkistetaan onko jakojäännökselle olemassa tarkistustunnus
        if ((checking_code >= 10) and (checking_code <= 30)) or ((checking_code >= 0) and (checking_code <= 9)):
            #jos aakkonen
            if (checking_code >= 10) and (checking_code <= 30):
                alphabet = "ABCDEFHJKLMNPRSTUVWXY"
                code = alphabet[checking_code - 10]
                code_type = "a"
            #jos numero
            if (checking_code >= 0) and (checking_code <= 9):
                code = int(checking_code)
                code_type = "n"
            #tarkistetaan täsmäävätkö tunnukset
            success = False
            if code_type == "a":
                if code == command[10]:
                    success = True
                else:
                    print("Tunnus ei ole kelvollinen")
            elif code_type == "n":
                if code == int(command[10]):
                    success = True
                else:
                    print("Tunnus ei ole kelvollinen")
            
            #jos täsmää
            if success == True:
                #selvitetään onko sama tunnus jo olemassa
                is_list = list.count(command)
                #tarkistetaan onko välilyönti ennen
                spaced_command = " " + command
                is_space = list.count(spaced_command)
                #jos edessä on välilyönti, luodaan uusi jono ilman sitä
                if is_space >= 1:
                    list2 = list.replace(spaced_command, command)
                #poistetaan tunnus
                if is_list >= 1:
                    if is_space >= 1:
                        list3 = list2.replace(command, "")
                        list = list3
                    else:
                        list2 = list.replace(command, "")
                        list = list2
                    print("Poistunut")
                #jos tunnus ei ole listassa (is_list)
                #tarkistetaan, onko tunnus eka (first)
                if (first == True) and (is_list < 1) and (is_space < 1):
                    list = command
                    first = False
                    print("Lisätty")
                #jos ei ole eka, niin lisätään edelliseen
                elif (first == False) and (is_list < 1) and (is_space < 1):
                    list = f"{list} {command}"
                    print("Lisätty")
                #tarkistetaan, alkaako lista välillä
                if list != "":
                    if list[0] == " ":
                        no_first_space = list[1:]
                        list = no_first_space
        else:
            print("Tunnus ei ole kelvollinen")
