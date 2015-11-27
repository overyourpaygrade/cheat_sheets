from segbuild import seg_builder
import argparse

if __name__ == '__main__':

  parser = argparse.ArgumentParser(description='hey')
  parser.add_argument('-cidr', dest='cidr', help='enter cidr!')
  args = parser.parse_args()

  if not args.cidr:
    print "Please enter a CIDR (ex: 192.168.1.0/24)"
    exit(1)

  seg_builder(args.cidr)
