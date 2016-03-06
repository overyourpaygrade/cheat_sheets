###### Table types
* FILTER - default table, contains built-in chains for:
    * INPUT - packages destined for local sockets
    * FORWARD - packets routed through the system
    * OUTPUT - packets generated locally
* NAT - is consulted when a packet tries to create a new connection
    * PREROUTING - used for altering a packet a soon its received
    * OUTPUT - used for altering locally gen packets
    * POSTROUTING - used for altering packets as they are about to go out
* MANGLE - packet altering
    * PREROUTING - altering incoming connections
    * OUTPUT - altering locally generated packets
    * INPUT - for incoming packets
    * POSTROUTING - altering packets as they are about to go out
    * FORWARD - for packets routed through the box

---

###### Start/Stop/Restart iptables
```
SystemD
* systemctl start iptables
* systemctl stop iptables
* systemctl restart iptables

SysVinit
* /etc/init.d/iptables start
* /etc/init.d/iptables stop
* /etc/init.d/iptables restart

```

###### Check all firewall rules
`iptables -L -n -v`

`iptables -t nat -L -v -n`

###### Block a specific IP address
```
iptables -A INPUT -s x.x.x.x -j DROP

iptables -A INPUT -p tcp x.x.x.x -j DROP

-A  append to table
-p  specify protocol

```

###### Unblock specific ipaddress
```
iptables -D INPUT -s x.x.x.x -j DROP

-D delete one or more from selected chain
```

###### Block a specific port
```
iptables -A OUTPUT -p tcp --dport xxx -j DROP

iptables -A INPUT -p tcp --dport xxx -j ACCEPT
```

###### Allow multiple ports
```
iptables -A INPUT -p tcp -m multiport --dports 20,80,443 -j ACCEPT

iptables -A OUTPUT -p tcp -m multiport --sports 22,80,443 -j ACCEPT
```

###### Allow network range
`iptables -A OUTPUT -p tcp -d 192.168.100.0/24 --dport 22 -j ACCEPT`

###### Block facebook
```
host facebook.com
facebook.com has address 66.220.156.68

whois 66.220.156.68 | grep CIDR
CIDR: 66.220.144.0/20

iptables -A OUTPUT -p tcp -d 66.220.144.0/20 -j DROP
```

###### Setup port forwarding
`iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 25 -j REDIRECT --to-port 2525`

###### Block network flood
`iptables -A INPUT -p tcp --dport 80 -m limit --limit 100/minute --limit-burst 200 -j ACCEPT`

###### Block Incoming ping requests
`iptables -A INPUT -p icmp -i eth0 -j DROP`

###### Allow lookback access
`iptables -A INPUT -i lo -j ACCEPT`

`iptables -A OUTPUT -o lo -j ACCEPT`

###### Log dropped packets (/var/log/messages)
`iptables -A INPUT -i eth0 -j LOG --log-prefix "IPtables dropped packets:"

###### Block a MAC address
`iptables -A input -m mac --mac-source AA:BB:CC:DD:EE:FF -j DROP`

###### Limit number of concurrent connections per IP
`iptables -A input -p tcp --syn --dport 22 -m connlimit --connlimit-above 3 -j REJECT`

###### Search within iptables rules
`iptables -L INPUT -v -n | grep 192.168.0.100`

###### Custom chain
`iptables -N custom-filter`

###### Flush iptables firewall chains or rules
`iptables -F`

`iptables -t nat -F`

###### Save iptables rules to a file
`iptables-save > ~/iptables.rules`

###### Restore iptables rules 
`iptables-restore < ~/iptables.rules`

###### Setup IPtables rules for PCI compliance
`iptables -I INPUT -d SITE -p tcp -m multiport --dports 21,25,110,143,465,587,993,995 -j DROP`

###### Allow established and related connections
```
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

iptables -A OUTPUT -m conntrack --ctstate ESTABLISHED -j ACCEPT
```

###### Drop invalid packets
`iptables -A INPUT -m conntrack --ctstate INVALID -j DROP`

###### Block connection on network interface
`iptables -A INPUT -i eth0 -s x.x.x.x -j DROP`

###### Disables outgoing mails
`iptables -A OUTPUT -p tcp --dports 25,465,587 -j REJECT`
