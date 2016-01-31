import hashlib
import time
import os
import itertools
import multiprocessing

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', '1']

SALT = "&45Bvx9"

PW_LOW = 4
PW_HIGH = 8

def pwGenerator(size):
  pwCount = 0
  try: 
    fp=open('PW- '+str(size), 'w')
    for r in range(size, size+1):
      for s in itertools.product(chars, repeat=r):
        pw=''.join(s)

        md5Hash = hashlib.md5()
        md5Hash.update(SALT+pw)
        md5Digest = md5Hash.hexdigest()

        fp.write(md5Digest + ' ' + pw + '\n')
        pwCount += 1
        del md5Hash
  except:
    print 'File/Hash Processing Error'
  finally:
    fp.close()
    print str(size), ' Passwords Processed = ', pwCount

if __name__ == '__main__':
  print 'Processing Multi-Core'
  print os.getcwd()
  print 'Password strings: ', chars
  print 'Password Lengths: ', str(PW_LOW), ' - ', str(PW_HIGH)

  startTime = time.time()

  corePool = multiprocessing.Pool(processes=5)

  results = corePool.map(pwGenerator, (0, 1, 2, 3, 4, 5, 6, 7, 8))

  elapsedTime=time.time() - startTime

#  elapsedTime=time.time() - startTime

  print 'Multi-Core Rainbow Complete'
  print 'Elapsed Time: ', elapsedTime
#  print 'Passwords Generated: ', pwCount
  print
