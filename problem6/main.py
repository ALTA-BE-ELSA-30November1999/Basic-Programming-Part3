
def full_prima(N):
    # your code here
    str_N = str(N)
    
    if N >= 1 :
        length = str_N[0]
        length_int = int(length)
        prima = True
        if length_int == 1  :
            prima = False
    
        for i in range (2, length_int) :
            if length_int % i == 0:
                prima = False

        Hasil = N % 10
        for x in range (2, Hasil) :
            if Hasil % x == 0 :
                prima = False
    else :
        prima = False

    return(prima)


if __name__ == '__main__':
    print(full_prima(2)) # True
    print(full_prima(3)) # True
    print(full_prima(11)) # False
    print(full_prima(13)) # False
    print(full_prima(23)) # True
    print(full_prima(29)) # False
    print(full_prima(37)) # True
    print(full_prima(41)) # False
    print(full_prima(43)) # False
    print(full_prima(53)) # True