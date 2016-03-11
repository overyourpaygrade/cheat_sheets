List all connections

`ss`

Filter tcp (a will show LISTENING)

`ss -ta`

Filter udp

`ss -u`

Filter unix socket connections

`ss -x`

Do not resolve hostnames

`ss -nt`

Show only LISTENING sockets

`ss -ltn`

`ss -lun`

Print process name and pid

`ss -ltp`

Summary statistics

`ss -s`

Display timer information

`ss -tn -o`

Display only IPv4 or v6 socket connections

`ss -tl -f inet`

`ss -tl6`

Filtering by tcp connection state

`ss -t4 state established`

`ss -t4 state time-wait`

Options:

```
1. established 
2. syn-sent 
3. syn-recv 
4. fin-wait-1 
5. fin-wait-2 
6. time-wait 
7. closed 
8. close-wait 
9. last-ack 
10. closing 
11. all - All of the above states 
12. connected - All the states except for listen and closed 
13. synchronized - All the connected states except for syn-sent 
14. bucket - Show states, which are maintained as minisockets, i.e. time-wait and syn-recv. 
15. big - Opposite to bucket state.
```

Watch for syns

`watch -n 1 "ss -t4 state syn-sent"`

Filter connections by address and port number

`ss -at '( dport = :ssh or sport = :ssh )'`

`ss -at '( dst = :443 or dst = :80 )'`

`ss -nt dst :443 or dst :80`

Filter by address

`ss -nt dst 74.125.236.178`

CIDR notation

`ss -nt dst 74.125.236.178/16`

Addreess and Port combined

`ss -nt dst 74.125.236.178:80`

Filter by port

`ss -nt dport = :80`

Source addr and src port gt than 5000

`ss -nt src 127.0.0.1 sport gt :5000`

Local smtp (port 25) sockets

`sudo ss -ntlp sport eq :smtp`

Port numbers greater than 25

`sudo ss -nt sport gt :1024`

Sockets with remote ports less than 100

`sudo ss -nt dport \< :100`

Connections to remote port 80

`sudo ss -nt state connected dport = :80`
