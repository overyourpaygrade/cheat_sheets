###### List shares (password when prompted)
* smbclient -L [target] -U [username] -p 445

###### Connect to share and interact
* smbclient //[target]/test -U [username] -p 445

###### list
* smb: \> ls

###### download
*  smb: \> get [filename]

###### Establish an SMB session
* rpcclient -U [username] [targetIP]

###### list users
* rpcclient $> enumdomusers

###### list groups
* rpcclient $> enumalsgroups

###### show all user sids defined on the box
* rpcclient $> lsaenumsid

###### show user or group SID
* rpcclient $> lookupnames

###### show username associated with SID
* rpcclient $> lookupsids

###### show OS type and version
* rpcclient $> srvinfo
