import hashlib
import time
import itertools
import multiprocessing

lowerCase = ['a','b','c','d','e','f','g','h']
upperCase = ['G','H','I','J','K','L']
numbers = ['0','1','2','3']
special = ['!','@','#','$']


allCharacters = []
allCharacters = lowerCase + upperCase + numbers + special

DIR = '/home/slasheks/pw/'

SALT = "&45Bvx9"

PW_LOW = 2
PW_HIGH = 6

def pwGenerator(size):
  pwList = []
  for r in range(size, size+1):
    for s in itertools.product(allCharacters, repeat=r):
      pwList.append(''.join(s))
  try:
    fp = open( DIR + str(size), 'w')
    for pw in pwList:
      md5Hash = hashlib.md5()
      md5Hash.update(SALT+pw)
      md5Digest = md5Hash.hexdigest()
      fp.write(md5Digest + ' ' + pw + '\n')
      del md5Hash
  except:
    print 'File Processing Error 1'
  finally:
    fp.close()

if __name__ == '__main__':
  startTime = time.time()
  corePool = multiprocessing.Pool(processes=4)

  results = corePool.map(pwGenerator, (2,3,4,5))
  pwDict = {}

  for i in range(PW_LOW, PW_HIGH):
    try:
      fp = open(DIR + str(i), 'r')
      for line in fp:
        pairs = line.split()
        pwDict.update({pairs[0] : pairs[1]})
      fp.close()
    except:
      print 'File Handling Error 2'
      fp.close()

  elapsedTime = time.time() - startTime
  print 'Elapsed Time: ', elapsedTime, 'Seconds'

  print 'Password Generated: ', len(pwDict)
  print
  cnt = 0
  for key, value in (pwDict.items()):
    print key, value
    cnt += 1
    if cnt > 10:
      break;
  print

  pw = pwDict.get('c6f1d6b1d33bcc787c2385c19c29c208')
  print 'Hash Value Tested = \ 2bca9b23eb8419728fdeca3345b344fc'
  print 'Associated Password = '
  print pw
