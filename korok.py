def beker():
    lista = []
    while len(lista) < 5:
        kor = int(input("Adja meg a kort:"))
        if kor >= 0 and kor <= 120:
            lista.append(kor)
        else:
            print("Csak 0 és 120 közötti kort lehet megadni!")

    return lista



def elso_idos(lista):
    i = 0

    while i < len(lista) and not lista[i] > 70:
        i += 1
    van = i < len(lista)
    # nincs = i >= len(lista)

    if van:
        return i
    else:
        return -1


def osszefuz(lista, elvalaszto):
    i = 0
    szoveg = ""
    while i <len(lista):
        if i == 0:
            szoveg = str(lista[i])
        else:
            szoveg += elvalaszto + str(lista[i])
        i += 1
    print(szoveg)


def konzolra_ir(lista):
    index = elso_idos(lista)
    print(f"Első idos ember korának indexe a listában: {index}")



def fajl_ir(lista, fajlnev):
    fh = open(fajlnev, "w", encoding="utf=8")
    index = elso_idos(lista)
    fh.write(f"Első idos ember korának indexe a listában: {index}")
    fh.close()
    print("A fájlba írás elkészült.")

