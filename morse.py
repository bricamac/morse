MORSE_CODE_DICT = { '' : '',
                    '.-' : 'A',
                    '-...' : 'B',
                    '-.-.' :'C',
                    '-..' : 'D',
                    '.' : 'E',
                    '..-.' : 'F',
                    '--.' : 'G',
                    '....' : 'H',
                    '..' : 'I',
                    '.---' : 'J',
                    '-.-' : 'K',
                    '.-..' : 'L',
                    '--' : 'M',
                    '-.' : 'N',
                    '---' : 'O',
                    '.--.' : 'P',
                    '--.-' : 'Q',
                    '.-.' : 'R',
                    '...' : 'S',
                    '-' : 'T',
                    '..-' : 'U',
                    '...-' : 'V',
                    '.--' : 'W',
                    '-..-' : 'X',
                    '-.--' : 'Y',
                    '--..' : 'Z'
                    }

def decode(message):

    morsedecoded=""
    for word in message.split():
        if word == "/":
            morsedecoded += " "
        elif word in MORSE_CODE_DICT:
                morsedecoded += MORSE_CODE_DICT[word]

    return morsedecoded
