
gombak_lista = []


def beolvasas():
    fajlom = open("gombak_jav.txt", "r", encoding="utf=8")
    fejlec = fajlom.readline()
    fajltartalom = fajlom.readlines()
    print(fajltartalom)
    fajlom.close()
    feldolgoz(fajltartalom)



def feldolgoz(fajltartalom):
    i = 0
    while (i < len(fajltartalom)):
        sor = fajltartalom[i].strip().split("@")
        print(sor)
        gombak_lista.append(gomba(sor))
        i += 1