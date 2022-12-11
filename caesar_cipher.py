import string, os, clipboard
from art import logo


#initialize global variables
CONT = True
LETTERS = []
#intialize variable with alphabet characters and * 2 for edge case
PRE_LETTERS = string.ascii_lowercase * 2


#convert strings to supplied lists
for letter in PRE_LETTERS:
    LETTERS.append(letter)


def caesar(start, shift, cipher):
    '''Basic cipher that takes three parameters: start, shirt, cipher'''
    result = ''
    if cipher == 'decode':
        shift *= -1

    for char in start:
        if char in LETTERS:
            position = LETTERS.index(char)
            new = position + shift
            result += LETTERS[new]

        else:
            result += char

    print(f'Here\'s the {cipher}d result: {result}')
    clipboard.copy(result)



#start caesar loop
try:
    while CONT:
        #clear screen and print logo
        os.system('clear')
        print(logo)

        #relevant queries
        cipher = input('Type "encode" to encrypt, type "decode" to decrypt:\n ~ ')
        start = input('Type your message:\n ~ ').lower()
        shift = int(input('Type the shift number:\n ~ '))

        #necessary shift to encode/decode
        shift = shift % 26

        #call function
        caesar(start, shift, cipher)

        #repeat or close loop and exit program
        restart = input('Type "yes" if you want to go again. Otherwise type "no".\n ~ ')
        if restart == 'no':
            CONT = False
            print('Goodbye')

except KeyboardInterrupt:
    print('\nSee you later.')