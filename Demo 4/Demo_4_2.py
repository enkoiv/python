def tarkasta_rivit(sudoku: list) -> bool:
    multiple = False

    #tarkastetaan onko sama numero useammin rivillä
    for i in sudoku:
        numbers = "123456789"
        found = ""
        for number in i:
            found += str(number)
        for i in numbers:
            count = found.count(i)
            if count > 1:
                multiple = True

    if multiple == True:
        return False
    else:
        return True

def tarkasta_sarakkeet(sudoku: list) -> bool:
    
    #luodaan sarakkeet
    sarakkeet = []
    for i in range(len(sudoku[0])):
        sarake = []
        for j in sudoku:
            sarake.append(j[i])
        sarakkeet.append(sarake)

    if tarkasta_rivit(sarakkeet) == True:
        return True
    else:
        return False

def tarkasta_pikkuruudukot(sudoku: list) -> bool:
    #tarkastetaan, että ruudukossa tietty numero esiintyy vain kerran
    #luodaan sudoku riveittäin: [1,2,3], [4,5,6]...
    sudoku_rows = []
    i = 0
    for i in range(len(sudoku)):
        first = sudoku[i][0:3]
        second = sudoku[i][3:6]
        third = sudoku[i][6:9]
        sudoku_rows.append(first)
        sudoku_rows.append(second)
        sudoku_rows.append(third)

    #järjestetään pikkuruudukoittain
    squares = []
    for i in range(3):
        squares.append(sudoku_rows[i])
        squares.append(sudoku_rows[i+3])
        squares.append(sudoku_rows[i+6])
    for i in range(9,12):
        squares.append(sudoku_rows[i])
        squares.append(sudoku_rows[i+3])
        squares.append(sudoku_rows[i+6])
    for i in range(18,21):
        squares.append(sudoku_rows[i])
        squares.append(sudoku_rows[i+3])
        squares.append(sudoku_rows[i+6])
    
    #tarkastetaan
    multiple = False
    j = 0
    while j <= 26:
        #luodaan ruudukko
        square = []
        square.append(squares[j])
        square.append(squares[j+1])
        square.append(squares[j+2])
        
        #luodaan ruudukosta str
        square_str = ""
        for i in range(len(square)):
            for k in square[i]:
                square_str += str(k)
        
        #tarkastetaan, onko samoja numeroita useampi
        numbers = "123456789"
        for i in numbers:
            count = square_str.count(i)
            if count > 1:
                multiple = True
        
        #siirrytään seuraavaan ruudukkoon
        j += 3
    
    if multiple == True:
        return False
    else:
        return True



def tarkasta_sudoku(lahde: str) -> bool:
    with open(lahde) as file:
        row_list = file.readlines()

        #poistetaan rivinvaihtomerkki
        counter = 0
        for i in row_list:
            row2 = i[:-1]
            row_list[counter] = row2
            counter += 1

        #tyhjät pois
        i = 0
        while i < len(row_list):
            if row_list[i] == "":
                del row_list[i]
            i += 1
        
        #tehdään ruudukko
        lista2 = []
        for i in row_list:
            lista = []
            for j in range(len(i)):
                lista.append(i[j])
            lista2.append(lista)

        #poistetaan pilkut ja välit
        for j in range(len(lista2)):
            i = 0
            while i < len(lista2[j]):
                if (lista2[j][i] == ",") or (lista2[j][i] == " "):
                    del lista2[j][i]
                i += 1

        #poistetaan välit uudelleen
        for j in range(len(lista2)):
            i = 0
            while i < len(lista2[j]):
                if (lista2[j][i] == " "):
                    del lista2[j][i]
                lista2[j][i] = int(lista2[j][i])
                i += 1

        sudoku = lista2

        if (tarkasta_rivit(sudoku) == True) and (tarkasta_sarakkeet(sudoku) == True):
            if (tarkasta_pikkuruudukot(sudoku) == True):
                return True
            else:
                return False
        else:
            return False

print(tarkasta_sudoku(r"C:\Users\eemel\Documents\Visual Studio\Teksti1.txt"))

# 1,2,3   4,5,6   7,8,9
# 7,8,9   1,2,3   4,5,6
# 4,5,6   7,8,9   1,2,3

# 5,1,2   6,4,7   9,3,8
# 9,3,4   8,1,5   2,6,7
# 8,6,7   9,3,2   5,1,4

# 2,4,8   3,7,1   6,9,5
# 3,9,5   2,6,4   8,7,1
# 6,7,1   5,9,8   3,4,2
