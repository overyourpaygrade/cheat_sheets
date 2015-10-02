###### Open a null session (protect creds)
* net use \\[target]\IPC$ /u:<domain>\<username> *

###### Run commands
* psexec [command]

###### Run a shell and shovel back
* psexec -u user -p pass \\[target] cmd.exe
