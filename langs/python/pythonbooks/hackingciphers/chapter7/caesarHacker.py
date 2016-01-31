#message = 'GUVF VF ZL FRPERG ZRFFNTR.'

message = raw_input('Enter the encrypted text: ')

message = message.upper()

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
  translated = ''
  for symbol in message:
    if symbol in LETTERS:
      num = LETTERS.find(symbol)
      num = num - key

      if num < 0:
        num = num + len(LETTERS)
      translated = translated + LETTERS[num]
    else:
      translated = translated + symbol

  print ('key #%s: %s' % (key, translated))
