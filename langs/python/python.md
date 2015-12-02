###### Execute command with python
``` python -c "print 'A'*52+'\xba\xdb\x01\x69'"```

###### CSV to Json
``` python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))" ```
 
###### Json to YAML
``` python -c 'import sys, yaml, json; yaml.safe_dump(json.load(sys.stdin), sys.stdout, allow_unicode=True)' < foo.json > foo.yaml ```

###### ASCII to HEX
``` python -c 'print "hello".encode("hex")'```

###### Decimal to HEX
``` python -c 'print hex(1337)'```

###### Decode Hex
``` python -c "print ''.join(chr(int(''.join(i), 16)) for i in zip(*[iter('474e552773204e6f7420556e6978')]*2))"```

###### Generate a random password
```` python -c 'import random; print "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*-_=+") for i in range(10)])'```

###### Generate a 18 character password, print the password and sha512 salted hash
``` cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 18 | head -1 | python -c "import sys,crypt; stdin=sys.stdin.readline().rstrip('\n'); print stdin;print crypt.crypt(stdin)"```

###### covert image to base64 string for data URI use
``` python -c 'print open("path/to/image.png", "rb").read().encode("base64").replace("\n","")' ```

###### Creates a simple web page for the current working directory over port 8000.
``` python -m SimpleHTTPServer ```

###### Module help print
``` python -c 'import paramiko ; help('paramiko')' ```
