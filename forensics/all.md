#### Forensic Tools
##### Foremost
###### Grab all supported file types
* foremost -t all file.raw

##### dd (Windows)
###### Image a Shadow Copy
* dd.exe if=\\.\\HarddiskVolumeShadowCopy4 of=F:\snapshot4.img --localwrt


#### IDS
##### Suricata
###### Analyze a pcap file
* suricata -c /etc/suricata/suricata-debian.yaml -r suspicious.pcap -l ./suricata_output

##### Snort
###### Analyze a pcap file
* snort -r suspicious.pcap -l ./snort_output -c /etc/snort/snort.conf

##### apache-scalp
###### Analyze log file for attacks and categorize
* python scalp-0.4.py -l /path/to/log/file.log -f default_filter.xml -o output_dir -html


#### Webmail
##### libpff (pffexport)
###### Extract quiet, output format all, export all (alloc, orphan, recovered)
* pffexport -q -f all -m all outlook.pst
