def piirrä_pelilauta():
    pass

def piirrä_kupu():
    pass

def alkuasetelma():
    pass

def piirrä_nappula(väri: str, rengas: int):
    pass

players = []
def pelaajanimet(nimi):
    players.append(nimi)

colors = []
def pelaajavärit(pelaaja: str, väri: str):
    index = players.find(pelaaja)
    colors[index] = väri

def ohjeet() -> str:
    pass

def arpakuutio(pelaaja: str) -> int:
    pass

def paina_kupua():
    pass

def korkein_numero(a: int, b: int, c: int, d: int) -> int:
    if (a > b) and (a > c) and (a > d):
        korkein = a
    elif (b > a) and (b > c) and (b > d):
        korkein = b
    elif (c > a) and (c > b) and (c > d):
        korkein = c
    else:
        korkein = d

def laske_renkaat(alku: int, loppu: int):
    pass

def vuoro(pelaaja: str):
    pass

def nappula_kotipesaan(indeksi: int):
    pass

def aseta_rengas(indeksi: int, väri: str):
    pass

def syo_nappula(syöjärengas: int, kohderengas: int):
    pass

def nappula_lahtoympyraan():
    pass

def vastustaja_lahtoympyrassa() -> bool:
    pass

def onko_kiertanyt(pelaaja) -> bool:
    pass

def onko_tasaluku(luku: int) -> bool:
    pass

def onko_nappuloita(pelaaja) -> bool:
    pass

def voittaja(pelaaja: str):
    pass
