###### Find and ignore unreadable directories
* find . ! -readable -prune

###### AV scan. Recurse and create a log
* clamscan -r -l scan.log /home/user
