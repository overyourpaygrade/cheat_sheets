###### Establish a session
* net use \\[target]

###### Connect as another user
* net use \\[targetIP]\[sharename] [password] /u:[UserName]

###### List shares
* net view \\[targetIP]

###### Null Session
* net use \\[targetIP] "" /u:""

###### Create an admin level account
* net user /add [user] [password]
* net localgroup administrators /add [user]

###### Delete an account
* net user [user] /delete

###### Map local drive letter to remote C$ (admin req)
* net use * \\[target]\c$ [admin pass] /u:[user]
* net use * \\[target]\C$ [password] /u:[targetIP]\[user] !W2K3

###### Delete all net use sessions
* net use * /d /y
