###### Find Files Using Name
* find -name "MyCProgram.c"

###### Find Files Using Name and Ignoring Case
* find -iname "MyCProgram.c"

###### Limit Search To Specific Directory Level Using mindepth and maxdepth
* find / -name passwd
* find / -maxdepth 2 -name passwd
* find / -maxdepth 3 -name passwd

###### Find the password file between sub-directory level 2 and 4.
* find -mindepth 3 -maxdepth 5 -name passwd

###### Executing Commands on the Files Found by the Find Command.
* find -iname "MyCProgram.c" -exec md5sum {} \;

###### Inverting the match.
* find -maxdepth 1 -not -iname "MyCProgram.c"

###### Finding Files by its inode Number.
* ls -li file
* find -inum 804180 -exec rm {} \;

##### Find file based on the File-Permissions
###### Find files which has read permission to group. World Readable
* find . -perm -g=r -type f -exec ls -l {} \;

###### Find files which has read permission only to group.
* find . -perm g=r -type f -exec ls -l {} \;

###### Find files which has read permission only to group [ search by octal ]
* find . -perm 040 -type f -exec ls -l {} \;

##### Find all empty files (zero byte file) in your home directory and its subdirectory
######
* find ~ -empty

###### List all the empty files only in your home directory.
* find . -maxdepth 1 -empty

###### List only the non-hidden empty files only in the current directory.
* find . -maxdepth 1 -empty -not -name ".*"

###### Finding the Top 5 Big Files
* find . -type f -exec ls -s {} \; | sort -n -r | head -5

###### Finding the Top 5 Small Files
* find . -type f -exec ls -s {} \; | sort -n  | head -5
* find . -not -empty -type f -exec ls -s {} \; | sort -n  | head -5

##### Find Files Based on file-type using option -type
###### Find only the socket files.
* find . -type s

###### Find all directories
* find . -type d

###### Find only the normal files
* find . -type f

###### Find all the hidden files
* find . -type f -name ".*"

###### Find all the hidden directories
* find -type d -name ".*"

###### Find files by comparing with the modification time of other file.
* find -newer ordinary_file

##### Find Files by Size
* Note: – means less than the give size, + means more than the given size, and no symbol means exact given size.

###### Find files bigger than the given size
* find ~ -size +100M

###### Find files smaller than the given size
* find ~ -size -100M

###### Find files that matches the exact given size
* find ~ -size 100M

[Resource](http://www.thegeekstuff.com/2009/03/15-practical-linux-find-command-examples/)
