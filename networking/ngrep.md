##### Network Forensics - Tracking Hackers Through Cyberspace

###### Usage
```ngrep -I capturefile.pcap "string to search for"```

###### Text with a filter (only from src and dst)
```ngrep -I capturefile.pcap "string" 'src host 192.168.1.20 and dst port 80'```

###### regular expression search for keywords
```ngrep -I evidence01.pcap 'secret|recipe|Ann'```
