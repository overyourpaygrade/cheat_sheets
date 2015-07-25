###### [Raw packet data field only](https://ask.wireshark.org/questions/15374/dump-raw-packet-data-field-only)
* tshark -r infile -T fields -e data | tr -d "\n" > tempfile

###### Get all Http user agent strings from pcap
* tshark.exe -r evidence03.pcap -T fields -e http.user_agent | egrep -v '^$'

###### Get all HTTP response lines
* tshark.exe -r evidence03.pcap -T fields -e http.response.line

###### Export as pdml
* tshark.exe -r evidence03.pcap -T pdml
