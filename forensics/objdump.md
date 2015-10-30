###### Display the contents of the overall file header
```objdump --file-headers ./hello.exe
or
objdump -f ./hello.exe```

###### Display the contents of the section headers
```objdump --section-headers ./brbbot.exe
or
objdump -h ./brbbot.exe```

###### Display the contents of all headers
```objdump -x ./brbbot.exe```

###### Display assembler contents of executable sections
```objdump -d ./brbbot.exe```

###### Display assembler contents of all sections
```objdump -D ./brbbot.exe```

###### Display the full contents of all sections
```objdump -s ./brbbot.exe```

###### Display the contents of symbol table (or tables)
```objdump -t ./brbbot.exe```

###### Display the contents of dynamic symbol table
```objdump -T ./brbbot.exe```

###### Display the dynamic relocation entries in the file
```objdump -R ./brbbot.exe```

###### Display section of interest
```objdump -s -j.text ./brbbot```

###### Resources
* http://www.thegeekstuff.com/2012/09/objdump-examples/
