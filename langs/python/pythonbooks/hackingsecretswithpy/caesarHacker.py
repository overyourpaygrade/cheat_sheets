# Caesar Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

message = 'GUVF VF ZL FRPERG ZRFFNTR.'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# loop through every possible key
for key in range(len(LETTERS)):

    # It is important to set translated to the blake string so that the
    # previous iteration value for translated is cleared.
    translated = ''

    # The rest of the program is the sam as the original caesar program:

    # run the cnryption/decryption program code on each symbol in the message
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) # get the number of the symbol
            num = num - key

            # handle the wrap around if num is 26 or larger than 0
            if num < 0:
	        num - num + len(LETTERS)

	    # add number's symbol at the end of translated
	    translated = translated + LETTERS[num]
        else:
            # just add the symbol without encrypting/decrypting
            translated = translated + symbol
    # display the current key being tested, along with its decryption
    print('key #%s: %s' % (key, translated))
