##### [LSOF](https://danielmiessler.com/study/lsof/)

###### See files and network connections a process has:
* lsof -c ncat

###### Same as above with PID
* lsof -p 2307

###### See things interacting with a directory
* lsof /home/stuff/private

###### With a file
* lsof /home/stuff/private/passwords/txt

###### Networking info based on port
* lsof -i :1337

###### Connections to a particular IP
* lsof -i@ 192.168.1.1

###### Connections to a host and port
* lsof -i@192.168.1.1:80

###### TCP Listen
* lsof -i -sTCP:LISTEN

###### TCP Established
* lsof -i -sTCP:ESTABLISHED

###### Show open files with a link count of less than 1 (hide file by unlinking)
* lsof +L1

