def h(h: int) -> str:
    numerot = ["yksi", "kaksi", "kolme", "neljä", "viisi", "kuusi", "seitsemän", "kahdeksan", "yhdeksän", "kymmenen", "yksitoista", "kaksitoista"]
    if h > 12:
        h -= 12
    if 1 <= h <= 12:
        return numerot[h - 1]

def min(min: int) -> str:
    if min == 45:
        return "varttia vaille"
    elif min == 15:
        return "varttia yli"
    elif min == 30:
        return "puoli"
    elif min > 30:
        return f"{60 - min} vailla"
    elif (min < 30) and (min != 0):
        return f"{min} yli"
    elif min == 0:
        return "tasan"

def tulosta_kello(tunnit: int, mins: int) -> str:
    if (30 <= mins < 60):
        tunnit += 1
    if (tunnit == 0) and (mins == 0):
        print("On keskiyö.")
    else:
        print(f"Kello on {min(mins)} {h(tunnit)}.")

while True:
    ho = int(input("Anna h: "))
    mins = int(input("Anna min: "))
    tulosta_kello(ho, mins)