# Ověření čísla platební karty podle tzv. Luhnova testu


# Vytvoř funkci, ve které uživatel zadá číslo karty
def input_card_number():
    card_number = input("Please, input your card number: ")
    return card_number


# Vytvoř funkci, která obrátí pořadí číslic v zadaném čísle karty
def reverse_card_number():
    card_number = input_card_number()
    reversed_card_number = card_number[::-1]
    # kontrola print
    print(reversed_card_number)
    return reversed_card_number


# Spočítej sumu všech čísel na lichých indexech obráceného čísla karty
# Vyber čísla na sudých indexech, vynásob je dvěma, sečti jednotlivé cifry 
# (dvojciferné rozděl na dvě čísla a sečti)
def count_sum_of_odd_index ():
    reversed_card_number = reverse_card_number()

    odd_index = reversed_card_number[::2]
    even_index = reversed_card_number[1::2]

    summary = 0
    for num in odd_index:
        summary += int(num)
    
    numbers = []
    for num in even_index:
        result = int(num) * 2
        numbers.append(result)


# Sečti sumy lichých a upravených sudých indexů


# Výslednou hodnotu vydělíš deseti a pokud bude zbytek po dělení nula, je číslo karty platné


