###### List of hives for the memory image:
* vol.py -f img.raw hivelist

###### Dump passwords in plain text (Win7 32/64bit)
* vol.py -f img.raw --profile=Win7SP1x86 mimikatz

###### Dump Process Memory
* python vol.py -f challenge.vmem pslist
* python vol.py -f challenge.vmem memdump -p 1568 --dump-dir=dump/
