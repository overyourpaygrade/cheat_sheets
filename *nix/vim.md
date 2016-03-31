###### Delete all lines
* :1,$d

###### Jump to the beginning 
* gg or 1G

###### Jump to the end
* G

###### Substitute
* :%s/foo/bar/g
* flags: g - all matches, i - case insensitive, c - confirm each match
* :%s/foo/bar/gic

###### Go to the particular pattern’s line inside the file,
* vim +/install README

###### Go to the particular pattern’s line inside the file,
* vim +?bug README

###### Go to the Nth line of the file after opening it.
* vim +10 /etc/passwd

###### Good color file
* Tomorrow-Night-Eighties.vim

###### Multiple Windows
```
 :e filename      - edit another file
 :split filename  - split window and load another file
 ctrl-w up arrow  - move cursor up a window
 ctrl-w ctrl-w    - move cursor to another window (cycle)
```
