##### MMLS
###### Show partition information 
* mmls img.dd

###### Show partition information on a split file (-i raw, aff, afd, afm, afflib, ewf)
* mmls -i raw file.E0*

##### FSSTAT
###### Partition information
* fsstat -o 10260 img.dd

##### FLS
###### Look at the root dir. 
* Dir entry/File Metadata - Inode/MFT Entry - Name
* fls -o 10260 img.dd

###### ADS
* fls -Fr -o 59 -f ntfs ntfs_pract.dd 

###### See only deleted entries that are liste as files, recursive
* fls -o 10260 -Frd img.dd
* F = file entries, r = recursive, d = deleted entries

##### ICAT
###### Data Blocks associated with a inode or MFT entry to stdout
* icat -o 10260 img.dd 2139 > file.ext.2139

###### Pipe to file to see the magic (dash = read from stdin)
* icat -o 10260 file.idd 11108 | file -

###### Pipe to imagemagik to view
* icat -o 10260 img.dd 11108 | display

###### Open a file in an alternate data stream (need fls MFT info)
* icat -o 59 -f ntfs ntfs.dd 137-128-4



###### References
* [Linux Leo](http://linuxleo.com/)
