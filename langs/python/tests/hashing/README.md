##### Hashing files with python

```

File size:  4.6G Sep 26 18:45 file.txt

Time difference:

$ time ./hasher.py -f file.txt
MD5  d6b6c4ef57d5169c8fb5a62eff021822
SHA1 0726189c52504673b8a901930dd200af055142ff

real    0m16.139s
user    0m13.499s
sys     0m2.640s

$ time sha1sum.exe file.txt
0726189c52504673b8a901930dd200af055142ff *file.txt

real    0m13.624s
user    0m11.500s
sys     0m2.108s

$ time md5sum.exe file.txt
d6b6c4ef57d5169c8fb5a62eff021822 *file.txt

real    0m9.733s
user    0m7.578s
sys     0m2.124s


```
