###### Server
* nc -l 2389

###### Client
* nc localhost 2389

###### Transfer files
* Regular:
  * nc -l 2389 > file (server)
  * cat file | nc localhost 2389

* With a progress bar:
  * cat file | pv -b | nc -l 2389
  * nc remote_host 2389 | pv -b > file

* Encrypted:
  * cat file.big | nc -l 2389
  * ssh -f -L 23899:127.0.0.1:2389 user@remote_host sleep 10; nc 127.0.0.1 23899 | pv -b > file.big

###### netcat UDP
* nc -4 -u -l 2389
* nc -4 -u localhost 2389

###### netcat port-scanner
* nc -z 10.10.10.15 80-125

###### Resources:
* [Link1](http://www.binarytides.com/netcat-tutorial-for-beginners/)
* [Link2](www.thegeekstuff.com/2012/04/nc-command-examples/)
* [Link3](http://www.admin-magazine.com/Articles/Pen-Testing-with-netcat)
