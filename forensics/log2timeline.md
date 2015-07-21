###### Parse a shortcut file
* log2timeline -f win_lnk -z EST5EDT link.lnk

###### Parse IE History
* log2timeline -r -z EST5EDT -f iehistory History.IE5 > timeline.csv

###### Parse the Recycle Bin
* log2timeline -z EDT5EST -f recycler /path-to/RECYCLER/\{SID\}/INFO2 > timeline.csv

###### NTUSER.DAT
* log2timeline -z EDT5EST -f ntuser ntuser.dat > timeline.csv

###### Office 2010 Files
* log2timeline -z EDT5EST -f oxml doc.docx > timeline.csv 
