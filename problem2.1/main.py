bilangan = int(input("Masukkan angka = "))

def Faktor (bilangan):
    List = []
    for x in range(1, bilangan+1) :
        if bilangan % x == 0 :
            List.append(x)
            print(x)
    return(List)

Bil_faktor = Faktor(bilangan)
# print (Bil_faktor)
# print (Bil_faktor[0])
# print (Bil_faktor[1])
# print (Bil_faktor[2])
# print (Bil_faktor[3])
# print (Bil_faktor[4])
# print (Bil_faktor[5])
# print (Bil_faktor[6])