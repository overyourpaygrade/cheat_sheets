Acquire the pubkey of the dev/app/org:
```
curl -O https://keybase.io/reichl/key.asc
```

Import the key
```
gpg --import key.asc
```

List the keys you have to make sure import worked
```
gpg --list-keys

pub   1024D/FEB7C7BC 2007-08-27
uid                  Dominik Reichl <dominik.reichl@gmx.de>
sub   4096g/F129EEB7 2007-08-27
```

Verify the file downloaded
```
gpg --verify KeePass-2.33.zip.asc

gpg: assuming signed data in `KeePass-2.33.zip'
gpg: Signature made Sat, May  7, 2016  5:19:45 AM EDT using DSA key ID FEB7C7BC
gpg: Good signature from "Dominik Reichl <dominik.reichl@gmx.de>"
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 2171 BEEA D0DD 92A1 8065  5626 DCCA A5B3 FEB7 C7BC
```
