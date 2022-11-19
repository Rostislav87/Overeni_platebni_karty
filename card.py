# Ověření čísla platební karty podle tzv. Luhnova testu
from num_of_card import reversed_card_number

# Spočítej sumu všech čísel na lichých indexech obráceného čísla karty
# Vyber čísla na sudých indexech, vynásob je dvěma, sečti jednotlivé cifry 
# (dvojciferné rozděl na dvě čísla a sečti)
def card_number():
    odd_index = reversed_card_number[::2]
    even_index = reversed_card_number[1::2]

    sum1 = 0
    for num in odd_index:
        sum1 += int(num)
    
    numbers = []
    for num in even_index:
        result = int(num) * 2
        numbers.append(result)

    list1 = []
    for number in numbers:
        if number > 9:
            number = int(str(number)[0]) + int(str(number)[1])
            list1.append(number)
        else:
            list1.append(number)    

    sum2 = sum(list1)
    return sum1 + sum2


# Sečti sumy lichých a upravených sudých indexů
def count():
    result = card_number()
    return result


# Výslednou hodnotu vydělíš deseti a pokud bude zbytek po dělení nula, je číslo karty platné
def validate_number():
    return count() % 10 == 0
       

print(validate_number())        
    

