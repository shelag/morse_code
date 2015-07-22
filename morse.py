import sys

import readline

choise = input('Writing sentences or morse code. (sentences/morse)')


code = {
    'A' : '.-',
    'B' : '-...',
    'C' : '-.-.',
    'D' : '-..',
    'E' : '.',
    'F' : '..-.',
    'G' : '--.',
    'H' : '....',
    'I' : '..',
    'J' : '.---',
    'k' : '-.-',
    'L' : '.-..',
    'M' : '--',
    'N' : '-.',
    'O' : '---',
    'P' : '.--.',
    'Q' : '--.-',
    'R' : '.-.',
    'S' : '...',
    'T' : '-',
    'U' : '..-',
    'V' : '...-',
    'W' : '.--',
    'Y' : '-.--',
    'Z' : '--..',
    '0' : '-----',
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9' : '----.',
    '.' : '.-.-.-',
    ',' : '--..--',
    '?' : '..--..',
    '"' : '.-..-.',
    '!' : '-.-.--',

}

def morse(frase):
    codemorse = ''
    for lettera in frase:
        if lettera in code.keys():
           codemorse = codemorse + ' ' + code[lettera]
    return codemorse

def reverse_morse(frase):
    new_frase = frase.split(' ')
    translate = ''
    for sig in new_frase:
        for k, v in code.items():
            if v == sig:
                translate += k
    return translate

if choise == 'sentences' or choise == 's':
    frase = input('writing sentences: ')
    upperf = frase.upper()
    print(morse(upperf))
elif choise == 'morse' or choise == 'm':
    frase_morse = input('writing morse code: ')
    print(reverse_morse(frase_morse))
else:
    choise = input('Writing sentences or morse code. (sentences/morse)')
