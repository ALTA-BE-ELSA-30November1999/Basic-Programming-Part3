bilangan = int(input("Masukkan angka = "))

def Faktor (bilangan):
    List = []
    for x in range(bilangan, 0, -1) :
        if bilangan % x == 0 :
            List.append(x)
            print(x)
    return(List)

Bil_faktor = Faktor(bilangan)