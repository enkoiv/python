coded_words = []
codes = []
numbers = "0123456789"
alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
specials = "!#%&/()=?"

def add_word():
    while True:
        word = input("Anna sana: ")
        if word == "":
            break

        is_number = False
        index = 0
        while index < 10:
            if word[-2] == numbers[index]:
                is_number = True
            index += 1
        
        index = 0
        is_small = 0
        while index <= len(word):
            lower = word.count(alphabet[index])
            is_small += lower
            index += 1
    
        index = 0
        is_upper = 0
        while index <= len(word):
            upper_alphabet = alphabet.upper()
            upper = word.count(upper_alphabet[index])
            is_upper += upper
            index += 1

        index = 0
        is_special = 0
        while index <= len(word):
            special = word.count(specials[index])
            is_special += special
            index += 1

        if (6 <= len(word) <= 8) and (is_number == True) and (is_small >= 1):
            if (is_upper >= 1) and (is_special >= 1):
                a = int(code[0])
                b = int(code[1])
                c = int(code[2])
                if len(word) % 2 == 0:
                    a_cha = word[a - 1]
                    print("a:", a_cha)
                    coded_word = word.replace(word[a - 1], word[-1])
                    print(coded_word)
                    coded_word2 = coded_word.replace(word[-1], a_cha)
                    print(coded_word2)
                    coded_words.append(coded_word2)
                    codes.append(code)
                    print("Lisätty")
                    print(coded_words)
                    print(codes)
                else:
                    c_cha = word[c - 1]
                    print("b:", b)
                    print("c:", c)
                    coded_word = word.replace(word[b - 1], word[c - 1])
                    coded_word2 = coded_word.replace(word[c - 1], c_cha)
                    coded_words.append(coded_word2)
                    codes.append(code)
                    print("Lisätty")
                    print(coded_words)
                    print(codes)
            else:
                print("Ei kelpaa")
        else:
            print("Ei kelpaa")
    add_code()


def add_code():
    while True:
        text = input("Anna koodausavain: ")
        index = 0
        count = 0
        while index < 10:
            add = text.count(numbers[index])
            count += add
            index += 1
        if (len(text) == 3) and (count == 3):
            if (1 <= int(text[0]) <= 5) and (1 <= int(text[1]) <= 5) and (1 <= int(text[2]) <= 5):
                print("OK")
                global code
                code = text
                add_word()
            else:
                print("Virhe")
        else:
            print("Virhe")
        if text == "":
            print("Lopetetaan")
            break

print("Syntaksi: oltava:aA!, pituus:6-8, [-2]=nro")
print("Avain: a,b,c=[1,5], abc")
print("%2=0: (a,-1); (b,c)")
add_code()