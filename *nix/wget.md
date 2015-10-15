###### Get recursive, 4 levels, no create directories, no host directories, accept pdf
* wget -r -l 4 -nd -nH -A pdf http://site.com/with-pdf

###### Download in the background
* wget -b http://www.openss7.org/repos/tarballs/strx25-0.9.2.1.tar.bz2

###### Change User Agent
* wget --user-agent="Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008092416 Firefox/3.0.3" URL-TO-DOWNLOAD

###### Check if the file exists
* wget --spider download-url

###### Resources
* http://www.thegeekstuff.com/2009/09/the-ultimate-wget-download-guide-with-15-awesome-examples/
* http://beatofthegeek.com/2011/08/download-in-geek-style-use-wget-part-2.html
