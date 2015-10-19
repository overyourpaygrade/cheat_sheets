###### Capture packets from a particular ethernet interface
* tcpdump -i eth0

###### Capture only N number of packets
* tcpdump -c 2 -i eth0

###### Display Captured Packets in ASCII
* tcpdump -A -i eth0

###### Display Captured Packets in HEX and ASCII
* tcpdump -XX -i eth0

###### Capture the packets and write into a file
* tcpdump -w 0.pcap -i eth0

###### Reading the packets from a saved file using
* tcpdump -r 0.pcap

###### Capture packets with IP address
* tcpdump -n -i eth0

###### Capture packets with proper readable timestamp
* tcpdump -n -tttt -i eth0

###### Read packets longer than N bytes
* tcpdump -w 0.pcap greater 1024

###### Receive only the packets of a specific protocol type
* tcpdump -i eth0 arp

###### Read packets lesser than N bytes
* tcpdump -w 0.pcap  less 1024

###### Capture packets for particular destination IP and Port
* tcpdump -i eth0 port 22

###### Capture TCP communication packets between two hosts
* tcpdump -w comm.pcap -i eth0 dst 16.181.170.246 and port 22

###### tcpdump Filter Packets – Capture all the packets other than arp and rarp
* tcpdump -i eth0 not arp and not rarp

###### Identify available interfaces
* tcpdump -D
 
###### Do not resolve names
* tcpdump -nn

###### Connections to a specific IP
* tcpdump -i eth0 -tttt dst 192.168.1.22 and not net 192.168.1.0/24

###### Resources 
* http://www.thegeekstuff.com/2010/08/tcpdump-command-examples/
