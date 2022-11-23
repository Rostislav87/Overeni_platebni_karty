Luhnův algoritmus je test, který používají některé bankovní společnosti k rozpoznání platného čísla kreditní karty od náhodně poskládaných číslic.

Jak pracuje Luhnův test na ukázce:

    Pracuješ s číslem karty: 49927398716,
    1. obrátíš pořadí číslic v zadaném čísle: 61789372994,
    2. suma číslic na lichých indexech: 6 + 7 + 9 + 7 + 9 + 4 = 42,
    3. vybereš číslice na sudých indexech, vynásobíš je dvěma, 
    4. sečteš jednotlivé cifry ve všech číslech a uděláš sumu: 1 8 3 2 9 --> 2 16 6 4 18 --> 2 7 6 4 9 = 28,
    5. sečteš sumy z kroků #2 a #4, 42 + 28 = 70
    6. výslednou hodnotu vydělíš deseti a pokud bude zbytek po dělení nula, je číslo platné. Tedy: 70 % 10 = 0.
