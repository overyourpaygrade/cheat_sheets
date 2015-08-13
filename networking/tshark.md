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
