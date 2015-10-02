###### Enumerate user accounts
* enum -U [target]

###### Password policy information
* enum -P [target]

###### Enumerate Groups
* enum -G [target]

###### Combine options
* enum -UGP [target]
 
###### List all shares (including admin)
* enum -S [target]

###### Dictionary attack against target (will lock out non-admin account [policy])
* enum -D -u [user] -f [wordfile] [target]

###### Connect to a target (default is NULL SMB session)
* enum -u [UserName] -p [password] -G [target]
