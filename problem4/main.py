def palindrome(input_string):
    Polidrome_is = False
    reverseKata = "".join(reversed(input_string)) #membalikkan string, join = menggabungkan
    if input_string == reverseKata :
        Polidrome_is = True
    return Polidrome_is
    # return 'error response'


if __name__ == '__main__':
    print(palindrome("civic")) # True
    print(palindrome("katak")) # True
    print(palindrome("kasur rusak")) # True
    print(palindrome("kupu-kupu")) # False
    print(palindrome("lion")) # False