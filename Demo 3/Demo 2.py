def tarkasta_rivit(sudoku: list) -> bool:
    multiple = False

    for i in sudoku:
        for row in i:
            if (row[0] == row[1]) and (row[0] != 0):
                multiple = True
            elif (row[0] == row[2]) and (row[0] != 0):
                multiple = True
            elif (row[1] == row[2]) and (row[0] != 0):
                multiple = True

    if multiple == True:
        return False
    else:
        return True

def tarkasta_sarakkeet(sudoku: list) -> bool:
    inverted = []

    for square in sudoku:
        inverted_i = []

        for i in range(0,3):
            column = []
            for row in square:
                column.append(row[i])
            inverted_i.append(column)
        
        inverted.append(inverted_i)
    
    if tarkasta_rivit(inverted) == True:
        return True
    else:
        return False

def tarkasta_sudoku(sudoku: list) -> bool:
    if (tarkasta_rivit(sudoku) == True) and (tarkasta_sarakkeet(sudoku) == True):
        return True
    else:
        return False

sudoku = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]

print(tarkasta_sudoku(sudoku))
