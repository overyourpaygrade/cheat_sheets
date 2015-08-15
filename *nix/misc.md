###### Find and ignore unreadable directories
* find . ! -readable -prune

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
