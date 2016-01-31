#message = 'Three can keep a secret, if two of them are dead.'

message = raw_input('Enter Message: ')

translated = ''

i = len(message) - 1
while i >= 0:
  translated = translated + message[i]
  i = i - 1

print(translated)
