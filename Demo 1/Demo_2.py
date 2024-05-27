print("Tervetuloa! Ohjelma antaa sivun otsikon")
print("Osoite annettava muodossa google.com")
print("Protokollan vaihto: http/https. Protokolla: https")
print("Osoitepääte: .com. Pois päältä: del. Pääte: <tyhjä>")
print("Ohjeet: help. Lista: list. Lopetus: <tyhjä>")
protocol = "https"
lever = True
titles = ""
end = "<tyhjä>"
lever2 = False

while True:
    other_command = False
    command = input("Anna osoite/komento: ")
    
    #ohjeteksti
    if command == "help":
        other_command = True
        print("*")
        print("Osoite annettava muodossa google.com")
        print("Protokollan vaihto: http/https. Protokolla:", protocol)
        print("Osoitepääte: .com. Pois päältä: del. Pääte:", end)
        print("Ohjeet: help. Lista: list. Lopetus: <tyhjä>")
        print("*")

    #lista
    if command == "list":
        other_command = True
        print("*")
        print("Lista: Osoite | Otsikko")
        print(titles)
        print("*")

    #lopetus
    if command == "":
        other_command = True
        print("Lopetetaan")
        break
    
    #protokolla
    if command == "http":
        other_command = True
        print("Protokolla: http")
        protocol = "http"
    elif command == "https":
        other_command = True
        print("Protokolla: https")
        protocol = "https"

    #osoitepääte
    if command == "del":
        other_command = True
        lever2 = False
        print("Pääte: <tyhjä>")
    if command[0] == ".":
        other_command = True
        end = command[0:]
        lever2 = True
        print("Pääte:", end)
    if lever2 == True:
        command += end

    #otsikon tallennus
    if other_command == False:
        
        #protokollan lisäys
        if protocol == "https":
            command = "https://www." + command
        elif protocol == "http":
            command = "http://www." + command

        #sivun tallennus
        from urllib.request import urlopen
        page = urlopen(command)
        content = str(page.read())

        #otsikon etsintä
        title_start = content.find("<title>")
        title_end = content.find("</title>")
        title = content[(title_start + 7):(title_end)]
        print("Sivun otsikko on", title)
        
        #otsikon lisäys listaan
        if lever == True:
            titles = f"{command} | {title}"
            lever = False
        elif lever == False:
            titles = f"{titles}\n{command} | {title}"