def sp_nainen_kieli_suomi() -> int:
    with open(r"C:\Users\eemel\Seafile\Yliopisto\TKO\Demo 4\vaestolaskenta_data.csv") as file:
        counter = 0
        ids = []
        for row in file:
            list = row.split(",")
            if list[0] == "\"id\"":
                pass
            elif list[0] in ids:
                if (list[2] != "\"2\"") and (list[4] != "\"1\""):
                    print("Nainen muuttanut sukupuolta tai äidinkieltä")
            else:
                if (list[2] == "\"2\"") and (list[4] == "\"1\""):
                    ids.append(list[0])
                    counter += 1
    print(f"1. Naiset, joiden kieli on suomi: {counter}")
    pause()

def perheen_koko_vahintaan_4() -> int:
    with open(r"C:\Users\eemel\Seafile\Yliopisto\TKO\Demo 4\vaestolaskenta_data.csv") as file:
        
        lines = [line for line in file]

    #listataan vuodet
    years = []
    for line in lines:
        list = line.split(",")
        if (list[1] in years) or (list[1] == '"vuosi"'):
            pass
        else:
            years.append(list[1])

    years = [int(year) for year in years]

    #lasketaan esiintymät vuosittain
    years_dict = {}
    for year in years:
        i = 0
        for line in lines:
            line2 = line.split(",")
            if (line2[0] != '"id"'):
                if (int(line2[6]) >= 4) and (int(line2[1]) == year):
                    i += 1
        years_dict[year] = i

    #tulostetaan
    printable = str(years_dict)[1:-1]
    print(printable)

def suuralueittain() -> str:
    with open(r"C:\Users\eemel\Seafile\Yliopisto\TKO\Demo 4\vaestolaskenta_data.csv") as file:
        lines = file.readlines()
    
    etela_suomi = 0
    lansi_suomi_ja_ahvenanmaa = 0
    ita_suomi = 0
    pohjois_suomi = 0

    years = [int(line.split(",")[1]) for line in lines if (line[0:4] != '"id"')]

    years2 = []
    for i in years:
        if i not in years2:
            years2.append(i)
    
    years = {}
    for year in years2:
        ids = []
        for line in lines:
            list = line.split(",")
            if (list[0] != '"id"') and (int(list[1]) == year):
                ids.append(list[0])
                if list[7] == "\"1\"":
                    etela_suomi += 1
                elif list[7] == "\"2\"":
                    lansi_suomi_ja_ahvenanmaa += 1
                elif list[7] == "\"3\"":
                    ita_suomi += 1
                elif list[7] == "\"4\"":
                    pohjois_suomi += 1

        years[year] = (etela_suomi, lansi_suomi_ja_ahvenanmaa, ita_suomi, pohjois_suomi)

    print("Suuralueittain:")
    for year in years:
        print(f"{year}: E-S: {years[year][0]} L-S/Ahv: {years[year][1]} I-S: {years[year][2]} P-S: {years[year][3]}")

def pause():
    blank = input("Paina Enter jatkaaksesi")

while True:
    print("")
    print("Valitse:")
    print("0. Poistu")
    print("1. Sp: nainen, kieli: suomi")
    print("2. Perheen koko väh. 4")
    print("3. Suuralueittain")

    choice = input("Valinta: ")

    if choice == "0":
        break

    if choice == "1":
        sp_nainen_kieli_suomi()
    elif choice == "2":
        perheen_koko_vahintaan_4()
    elif choice == "3":
        suuralueittain()