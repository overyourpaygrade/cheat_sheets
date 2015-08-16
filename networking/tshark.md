###### [Raw packet data field only](https://ask.wireshark.org/questions/15374/dump-raw-packet-data-field-only)
* tshark -r infile -T fields -e data | tr -d "\n" > tempfile

###### Get all Http user agent strings from pcap
* tshark.exe -r evidence03.pcap -T fields -e http.user_agent | egrep -v '^$'

###### Get all HTTP response lines
* tshark.exe -r evidence03.pcap -T fields -e http.response.line

###### Export as pdml
* tshark.exe -r evidence03.pcap -T pdml

###### Search PCAP for Zip Files
* tshark  -Y "http matches \"\x50\x4B\x03\x04\"" -r with_zip.pcap -x
* tshark  -Y "http contains "50:4B:03:04"" -r with_png.pcap


#### [DEF CON 22 - Home Alone with localhost: Automating Home Defense ](https://www.youtube.com/watch?v=2IeU7Cck0hI)
###### Speciifc devicels recieved signal strength indicator (RSSI)
* tshark -i mon0 -f "wlan src host <WLAN MAC>" -l -T fields -e radiotap.dbm_antsignal

###### All devices visible and their RSSI:
* tshark -i mon0 -l -T fields -e radiotap.dbm_antsignal -e wlan.sa

###### All fields available for a specific device
* tshark -i mon0 -f "wlan src host <WLAN MAC>" -l -T pdml
