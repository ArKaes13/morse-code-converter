morse_code = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ',': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '"': '.-..-.',
    ':': '---...',
    "'": '.----.',
    '-': '-....-',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '!': '-.-.--',
}

is_on = True
while is_on:
    selection = input('Enter "1" to convert text to morse code\nEnter "2" to convert morse code to text\nEnter "3" to Exit: ')
    if selection == '1':
        text = input('Enter the text you would like converted to morse code: ').lower()
        morse = []
        morse_string = ''
        for char in text:
            try:
                morse += morse_code[char]
                morse += ' '
            except KeyError:
                morse += '/'
                morse += ' '

        for char in morse:
            morse_string += char

        print(f'Encoded Text: {morse_string}\n')

    elif selection == '2':
        morse = input('Enter the morse code you would like converted to text. Letters must be separated by spaces '
                      'and words must be separated by forward slashes "/": ')
        morse_list = morse.split()
        text = ''
        values = list(morse_code.values())

        for code in morse_list:
            if code == '/':
                text += ' '
            else:
                index = values.index(code)
                text += list(morse_code.keys())[index]
        print(f'Decrypted Text: {text}\n')

    else:
        is_on = False
        print('Goodbye')