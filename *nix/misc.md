###### AV scan. Recurse and create a log
* clamscan -r -l scan.log /home/user

###### Find the entropy of a word
* echo administrator | ent

###### Find in files (current directory). Show File of match, line and recurse.
* grep -inr ntuser.dat

###### Find in binary file (treat as text), insensitive, and output byte offset
* grep -abi "string" img.dd

###### Copy (sync and archive, preserve properties), verbose with progress. Drop in dir2
* rsynv -avP dir/ dir2

###### Shows all the shortcuts available in Bash.
* bind -p

###### Flush the content of a text file, in a single go, from the command prompt.
* > file.txt

###### Enable IP Forwarding
echo "1" > /proc/sys/net/ipv4/ip_forward

###### Add DNS server
echo "nameserver 8.8.8.8" >> /etc/resolv.conf

#### For my.profile or bash.profile
###### Avoid duplicates
* export HISTCONTROL=ignoredups:erasedups 

###### When the shell exits, append to the history file instead of overwriting it
* shopt -s histappend
 
###### After each command, append to the history file and reread it
* export PROMPT_COMMAND="${PROMPT_COMMAND:+$PROMPT_COMMAND$'\n'}history -a; history -c; history -r"

###### history bash
* export PROMPT_COMMAND='history -a'

###### Remove sudo privileges from user
`sudo deluser username sudo`

###### Add sudo privileges to user
`gpasswd -a username sudo`
