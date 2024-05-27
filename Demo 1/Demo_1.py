answer = 0

while True:
    print("Tulos on nyt", answer)
    operation = input("Operaatio: ")

    if operation[0] == "+":
        answer += int(operation[1:])
    elif operation[0] == "-":
        answer -= int(operation[1:])
    elif operation[0] == "*":
        if (operation[0-1] == "*0") or (answer == 0):
            answer = 0
        else:
            answer = answer * int(operation[1:])
    elif operation[0] == "/":
        answer = int(answer) // int(operation[1:])

    if operation == "lopeta":
        print("Kiitos!")
        break