#!/usr/bin/env python

special_numbers = [1,2,3,5,8,9]
special_numbers_2 = [12]

def cardinal(num: int) -> str:
    if num % 100 in special_numbers_2:
        return f'{num // 100} {ordinal(num % 100)}'
    elif num % 10 in special_numbers:
        return f'{num // 10} {ordinal(num % 10)}'
    return ordinal(num) + 'th'

def ordinal(num: int) -> str:
    ones = {0 : 'zero',
            1 : 'one',
            2 : 'two',
            3 : 'three',
            4 : 'four',
            5 : 'five',
            6 : 'six',
            7 : 'seven',
            8 : 'eight',
            9 : 'nine',
            }
    twos = {10 : 'ten',
            20 : 'twenty',
            30 : 'thirty',
            40 : 'forty',
            50 : 'fifty',
            60 : 'sixty',
            70 : 'seventy',
            80 : 'eighty',
            90 : 'ninety'}
    magnitude = {0 : None,
                          1 : None,
                          2 : 'hundred',
                          3 : 'thousand',
                          4 : 'million',
                          5 : 'billion',
                          6 : 'trillion',
                          8 : 'quadrillion'}
    funny_numbers = {11 : 'eleven',
                     12 : 'twelve',
                     13 : 'thirteen',
                     14 : 'fourteen',
                     15 : 'fifteen',
                     16 : 'sixteen',
                     17 : 'seventeen',
                     18 : 'eighteen',
                     19 : 'nineteen'}
    def last2(num) -> str:
        if num in funny_numbers:
            return funny_numbers[num]
        if num < 10:
            return ones[num]
        if num % 10 == 0:
            return twos[num]
        return f'{twos[10 * (num // 10)]} {ones[num % 10]}'

    def three_digits(num) -> str:
        if num // 100 > 0:
            return f'{ones[num // 100]} hundred {last2(num % 100)}'
        return f'{last2(num % 100)}'

    def printer(num, depth = 0):
        return f'{printer(num // 1000, depth + 1)} {magnitude[depth]}{three_digits(num % 1000)}'



    return f'{printer(num)}'
