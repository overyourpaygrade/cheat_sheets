---

List the contents of a tar file

`tar -tvf file.tar`

List the contents of a tar.gz file

`tar -ztvf file.tar.gz`

List the contents of a tar.bz2 file

`tar -jtvf file.tar.bz2`

---

Flags

```
-t  list contents of an archive
-v  verbose
-z  filter the archive through gzip
-j  filter the archive through bzip2
-f  filename to use
```

---

Extract, gz, verbose, file, stdout

`tar xzvf file.tgz dir/README > dir/README`

Extract tar.bz2

`tar -xvjf file.tar.gz2`

Extract to a specific dir

`tar -xvzf file.tar.gz -C /this/dir`

Extract a single file

`tar -xz -f file.tar.gz "./dir/file.txt"`

`tar -xv -f file.tar.gz "./dir/file1.txt" "./dir/file2.txt"`

Extract multiple files using wildcards

`tar -xv -f file.tar.gz --wildcards "*.txt"`

---

Create a tar/tar.gz archive

`tar -cvf file.tar ./dir/`

Ask for confirmation before adding files

`tar -czw -f file.tgz ./dir/*`

Add files to existing archives (cannot be added to compressed archives)

`tar -rv -f file.tar file.txt`

Add files to compressed (workaround)

```
gunzip file.tgz
tar -rf file.tgz ./dir/file.txt
gzip file.tar
```

Backup with tar

`tar -cvz -f file-$(date +%Y%m%d).tgz ./dir/`

Verify archive files while creating (does not work with compressed archives)

`tar -cvW -f file.tar ./dir/`

---

http://www.binarytides.com/linux-tar-command/
