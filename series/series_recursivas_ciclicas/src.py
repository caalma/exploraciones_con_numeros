#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from sys import argv
from random import randint

palabras = {
    'espanol': ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve'],
    'ingles': ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'],
    'frances': ['zéro', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf'],
    'aleman': ['null', 'eins', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun'],
    'japonés': ['zero', 'ichi', 'ni', 'san', 'shi', 'go', 'roku', 'shichi', 'hachi', 'kyuu'],
    'chino': ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu'],
    'arabe': ['sifr', 'waahid', 'ithnaan', 'thalaathah', "arba'ah", 'khamsah', 'sittah', "sab'ah", 'thamaaniyah', "tis'ah"],
    'ruso': ["nol'", 'odin', 'dva', 'tri', 'chetire', "pyat'", "shest'", "sem'", "vosem'", "devyat'"],
    'italiano': ['zero', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove'],
    'portugues': ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove'],
    'holandes': ['nul', 'een', 'twee', 'drie', 'vier', 'vijf', 'zes', 'zeven', 'acht', 'negen'],
    'sanscrito': ['śūnya', 'eka', 'dvi', 'tri', 'catvāri', 'pañca', 'ṣaṭ', 'sapta', 'aṣṭa', 'nava'],
    'finlandes': ['nolla', 'yksi', 'kaksi', 'kolme', 'neljä', 'viisi', 'kuusi', 'seitsemän', 'kahdeksan', 'yhdeksän'],

    'identidad': ['', '1', '22', '333', '4444', '55555', '666666', '7777777', '88888888', '999999999'],
    'inverso': ['999999999', '88888888', '7777777', '666666', '55555', '4444', '333', '22', '1', ''],
    'random': ['a'*randint(0, 9) for i in range(0, 10)],
    }

def tr(n):
    return ''.join([str(len(d[int(v)])) for v in str(n)])


n = [argv[1] if len(argv) >= 2 else '0123456789']
d = palabras[argv[2] if len(argv) >= 3 else 'random']

limite_de_busqueda = 10000
limite_superado = False
ciclo_de_repeticion = []
ciclo_detectado = False

while True:
    x = tr(n[-1])
    if x == n[-1]:
        break
    else:
        n.append(x)
    if len(n) > 2:
        m = n[:-1][::-1]
        if x in m:
            ciclo_de_repeticion =  n[-1 - m.index(n[-1]):]
            if len(ciclo_de_repeticion) > 0:
                ciclo_detectado = True
                break
    if len(n) > limite_de_busqueda:
        limite_superado = True
        break

print(f'------------------------\n:: {n}\n')
print(f'Con el alfabeto:\n{d}\n')

if len(ciclo_de_repeticion) == 0:
    print(f'Se estabiliza en {n[-1]}\n')
else:
    print(f'Ciclo de {len(ciclo_de_repeticion)} pasos:\n{ciclo_de_repeticion}\n')

if(limite_superado):
    print(f'Límite de búsqueda superado ({limite_de_busqueda})\n')
