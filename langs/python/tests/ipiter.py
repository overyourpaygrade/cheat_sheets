# IP segment enumeration hack

import argparse
import re

dict = {
  '23' : 512,
  '24' : 256,
  '25' : 128,
  '26' : 64,
  '27' : 32,
  '28' : 16,
  '29' : 8
}

def main():

  if dict[mask] == 512:
    if int(cidr[3]) == 0:
      counter = 0
      third = int(cidr[2])
      for x in range(0, 2):
        for ip in range(int(cidr[3]),dict[mask]-256):
          formatted = '{}.{}.{}.{}'.format(cidr[0],cidr[1],third,str(ip))
          ipList.append(formatted)
          counter += 1
          if counter > 255:
            third = third + 1 
            counter = 0
            break
  else:
    for ip in range(int(cidr[3]),dict[mask]):
      formatted = '{}.{}.{}.{}'.format(cidr[0],cidr[1],cidr[2],str(ip))
      ipList.append(formatted)


  for ip in ipList:
    print ip


if __name__ == '__main__':

  parser = argparse.ArgumentParser(description='hey')
  parser.add_argument('-cidr', dest='cidr', help='enter cidr!')
  args = parser.parse_args()

  if not args.cidr:
    print "Please enter a CIDR (ex: 192.168.1.0/24)"
    exit(1)

  ipList = []
  cidr = re.findall(r"[\w]+", args.cidr)
  mask = cidr[4]
  ismask = mask in dict

  if ismask == False:
    print "Mask not supported or invalid"
    exit(1)

  main()
