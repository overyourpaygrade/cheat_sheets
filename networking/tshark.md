###### [Raw packet data field only](https://ask.wireshark.org/questions/15374/dump-raw-packet-data-field-only)
* tshark -r infile -T fields -e data | tr -d "\n" > tempfile
