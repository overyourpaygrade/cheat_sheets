###### Ping Scan - no priv
* nmap -sP 10.10.10.0/24

###### SYN scan - no priv
* nmap 10.10.10.0/24

###### OS Fingerprint
* nmap -O 10.10.10.15

###### DNS resolve (hostname) - no priv
* nmap -sL 10.10.10.0/24

###### TCP Syn and UDP Scan (-PN skips ping scan)
* nmap -sS -sU -PN 10.10.10.15

###### Port Range Scan
* nmap -p 1025-65535

###### TCP Connect (OS will establish the connection with connect()) - no priv
* nmap -sT 10.10.10.15

###### Aggresive Scan (noise!) (-T slow 0-5 fast) (-A OS and version checking) - no priv
* nmap -T4 -A 10.10.10.0/24

###### Fast Scan (common 100) - no priv
* nmap -T4 -F 10.10.10.15

###### Verbose!
* nmap -T4 -A -v 10.10.10.15

###### NMAP Scan Options
* -sT ( TcpConnect )  
* -sS ( SYN scan ) 
* -sF ( Fin Scan )
* -sX ( Xmas Scan ) 
* -sN ( Null Scan ) 
* -sP ( Ping Scan )
* -sU ( UDP scans ) 
* -sO ( Protocol Scan )  
* -sI ( Idle Scan )
* -sA ( Ack Scan ) 
* -sW ( Window Scan )  
* -sR ( RPC scan )
* -sL ( List/Dns Scan 

###### Ping detection
* -P0 ( don’t ping ) 
* -PT ( TCP ping ) 
* -PS ( SYN ping )
* -PI ( ICMP ping ) 
* -PB  (= PT + PI )
* -PP ( ICMP timestamp )  
* -PM ( ICMP netmask )

http://bencane.com/2013/02/25/10-nmap-commands-every-sysadmin-should-know/
