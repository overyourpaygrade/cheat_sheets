# IP segment enumeration hack
import re

def seg_builder(input_str):
  
  ipList = []
  cidr = re.findall(r"[\w]+", input_str)
  mask = cidr[4]

  dict = {
    '23' : 512,
    '24' : 256,
    '25' : 128,
    '26' : 64,
    '27' : 32,
    '28' : 16,
    '29' : 8,
    '30' : 4
  }
  
  ismask = mask in dict

  if ismask == False:
    print "Mask not supported or invalid"
    exit(1)

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
    counter = 0
    third = int(cidr[3])
    for ip in range(dict[mask]):
      formatted = '{}.{}.{}.{}'.format(cidr[0],cidr[1],cidr[2],third+counter)
      ipList.append(formatted)
      counter += 1
      if third + counter > 256:
        print "Outise the range or segment not valid"
        exit(1)

  for ip in ipList:
    print ip
