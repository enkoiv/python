potilaat = {}

def lisaa_potilas(tietokanta: str, asiakasnumero: str, nimi: str, laji: str, syntymaaika: str, syy: str):
    tietokanta[asiakasnumero] = (nimi, laji, syntymaaika, syy)

def onko_potilas(tietokanta: str, asiakasnumero: str) -> bool:
    success = False
    for avain in tietokanta:
        if avain == asiakasnumero:
            success = True
    if success == True:
        return True
    else:
        return False

def poista_potilas(tietokanta: str, asiakasnumero: str) -> bool:
    if onko_potilas(tietokanta, asiakasnumero) == True:
        del tietokanta[asiakasnumero]
        print("Poistettiin.")
    else:
        print("Ei löytynyt.")

def tulosta_lista(lista: list) -> str:
    first = True
    for i in lista:
        if first == True:
            first = False
            tuloste = i
        else:
            tuloste += ", " + i
    print(tuloste)

while True:
    print("Valitse:")
    print("1. Lisää")
    print("2. Poista")
    print("3. Etsi")
    print("0. Poistu")
    choice = int(input("Valinta: "))

    if choice == 0:
        break

    if choice == 1:
        customer = input("Asiakasnumero: ")
        name = input("Nimi: ")
        type = input("Laji: ")
        birthday = input("Syntymä-aika: ")
        reason = input("Syy: ")
        lisaa_potilas(potilaat, customer, name, type, birthday, reason)
    
    if choice == 2:
        customer = input("Asiakasnumero: ")
        poista_potilas(potilaat, customer)

    if choice == 3:
        print("Valitse (voit etsiä arvon osalla):")
        print("1. Asiakasnumero")
        print("2. Nimi")
        print("3. Laji")
        print("4. Käynnin syy")
        print("5. Syntymäaika")
        choice2 = int(input("Valinta: "))
        list = []
        list2 = []

        if choice2 == 1:
            customer = input("Asiakasnumero: ")
            for asiakasnumero in potilaat:
                if customer in potilaat:
                    list.append(asiakasnumero)
                    list2.append(potilaat[asiakasnumero][0])
            tulosta_lista(list)
            tulosta_lista(list2)

        if choice2 == 2:
            name = input("Nimi: ")
            for asiakasnumero in potilaat:
                if name in potilaat[asiakasnumero][0]:
                    list.append(asiakasnumero)
                    list2.append(potilaat[asiakasnumero][0])
            tulosta_lista(list)
            tulosta_lista(list2)

        if choice2 == 3:
            type = input("Laji: ")
            for asiakasnumero in potilaat:
                if type in potilaat[asiakasnumero][1]:
                    list.append(asiakasnumero)
                    list2.append(potilaat[asiakasnumero][1])
            tulosta_lista(list)
            tulosta_lista(list2)

        if choice2 == 4:
            reason = input("Syy: ")
            for asiakasnumero in potilaat:
                if reason in potilaat[asiakasnumero][3]:
                    list.append(asiakasnumero)
                    list2.append(potilaat[asiakasnumero][3])
            tulosta_lista(list)
            tulosta_lista(list2)

        if choice2 == 5:
            reason = input("Syntymäaika: ")
            for asiakasnumero in potilaat:
                if reason in potilaat[asiakasnumero][2]:
                    list.append(asiakasnumero)
                    list2.append(potilaat[asiakasnumero][2])
            tulosta_lista(list)
            tulosta_lista(list2)
