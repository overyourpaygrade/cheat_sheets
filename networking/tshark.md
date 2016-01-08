##### Network Forensics - Tracking Hackers Through Cyberspace
###### Basic read from file
```tshark -r capturefile.pcap```

###### Disable name resolution
```tshark -n -r capturefile.pcap```

###### PDML (Packet Details Markup Language) output
```tshark -r capturefile.pcap -T pdml```

###### Print a specific field defined by Wireshark proto dissector
```tshark -r capturefile.pcap -T fields -e frame.number -e ip.addr -e udp```

###### Use Wireshark "Decode As" functionality (port 29008 as http)
```tshark -r capturefile.pcap -d tcp.port==29008,http```

###### Use Wireshark filters
```tshark -r capturefile.pcap -R 'ip.addr == 192.168.1.1'```

###### BPF (Berkley Packet Filter)
```tshark -r capturefile.pcap 'host 192.168.1.1'```

###### LUA plugins (Franck’s OFT Lua protocol dissector)
```tshark -r evidence01.pcap -X lua_script:oft-tsk.lua -R "oft" -n -R frame.number==112```

###### Verbose option
```tshark -r evidence01.pcap -X lua_script:oft-tsk.lua -R "oft" -n -R frame.number==112 -V```

###### PDML output
```tshark -r evidence01.pcap -X lua_script:oft-tsk.lua -R "oft" -n -R frame.number==112 -T pdml```

###### Specific fields (filename and total size)
```
tshark -r evidence.pcap -X lua_script:oft-tsk.lua -R "oft" -n -T fields -e "oft.filename" -e oft.totsize -R frame.number==112
recipe.docx 12008
```

###### Wireshark filter for src and dst
```tshark -r capturefile.pcap -R "ip.src==192.168.1.158 && ip.dst==192.168.1.10"```

----

###### [Raw packet data field only](https://ask.wireshark.org/questions/15374/dump-raw-packet-data-field-only)
```tshark -r infile -T fields -e data | tr -d "\n" > tempfile```

###### Get all Http user agent strings from pcap
```tshark.exe -r evidence03.pcap -T fields -e http.user_agent | egrep -v '^$'```

###### Get all HTTP response lines
```tshark.exe -r evidence03.pcap -T fields -e http.response.line```

###### Export as pdml
```tshark.exe -r evidence03.pcap -T pdml```

###### Search PCAP for Zip Files
```tshark  -Y "http matches \"\x50\x4B\x03\x04\"" -r with_zip.pcap -x```
```tshark  -Y "http contains "50:4B:03:04"" -r with_png.pcap```

----

#### [DEF CON 22 - Home Alone with localhost: Automating Home Defense ](https://www.youtube.com/watch?v=2IeU7Cck0hI)
###### Speciifc devicels recieved signal strength indicator (RSSI)
```tshark -i mon0 -f "wlan src host <WLAN MAC>" -l -T fields -e radiotap.dbm_antsignal```

###### All devices visible and their RSSI:
```tshark -i mon0 -l -T fields -e radiotap.dbm_antsignal -e wlan.sa```

###### All fields available for a specific device
```tshark -i mon0 -f "wlan src host <WLAN MAC>" -l -T pdml```
