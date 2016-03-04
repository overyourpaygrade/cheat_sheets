###### Generate the keys
`ssh-keygen -t rsa`

###### Store the keys and add a passphrase
`Enter file in which to save the key (/home/user/.ssh/id_rsa):`

`Enter passphrase (empty for no passphrase):`

###### Copy the key
`ssh-copy-id pi@123.45.56.78`

`cat ~/.ssh/id_rsa.pub | ssh pi@123.45.56.78 "mkdir -p ~/.ssh && cat >>  ~/.ssh/authorized_keys"`

###### Disable root login
```
/etc/ssh/sshd_config

ChallengeResponseAuthentication no
PasswordAuthentication no
UsePAM no

/etc/init.d/sshd restart
```
