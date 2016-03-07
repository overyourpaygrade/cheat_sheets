List verbose tcp port 80

`fuser -v -n tcp 80`

Kill process listening on 80/tcp, confirm

`fuser -i -k 80/tcp`

Kill w/o confirmation

`fuser -k 80/tcp`

