def prime_number(num):
    prima = "Prime"
    if num == 1 :
        prima = "Not Prime"
    for x in range (2, num) :
        if num % x == 0 :
            prima = "Not Prime"
    # return (prima)
    return prima

if __name__ == '__main__':
    print(prime_number(11)) # "Prime"
    print(prime_number(13)) # "Prime"
    print(prime_number(17)) # "Prime"
    print(prime_number(20)) # "Not Prime"
    print(prime_number(35)) # "Not Prime"