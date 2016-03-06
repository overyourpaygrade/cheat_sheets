###### Extract, gz, verbose, file, stdout
`tar xzvfO file.tgz dir/README > dir/README`

###### List the contents of a tar file
`tar -tvf file.tar`

###### List the contents of a tar.gz file
`tar -ztvf file.tar.gz`

###### List the contents of a tar.bz2 file
`tar -jtvf file.tar.bz2`

---

###### Flags
```
-t  list contents of an archive
-v  verbose
-z  filter the archive through gzip
-j  filter the archive through bzip2
-f  filename to use
```
