###### Used to start a service (not reboot persistent)
```systemctl start service```

###### Used to stop a service (not reboot persistent)
```systemctl stop service```

###### Stop and start a service
```systemctl restart service```

###### Reload config file when supported
```systemctl reload service```

###### Restart if already running
```systemctl condrestart service```

###### Check status of service
```systemctl status service```

###### List services that can be started or stopped
```
systemctl
systemctl list-unit-files --type=service
ls /lib/systemd/system/*.service
/etc/systemd/system/*.service
```

###### Turn service on, for start at next boot or other trigger
```systemctl enable service```

###### Turn service off for the next reboot or other trigger
```systemctl disable service```

###### Check if service is configured to start or not
```systemctl is-enabled service```

###### Printable table of services that lists which runlevels each is configured on or off
```
systemctl list-unit-files --type=service
ls /etc/systemd/system/*.wants/
```

###### Used to list what levels this service is configured on or off
```ls /etc/systemd/system/*.wants/service.service```

###### Used when you create a new service file or modify any configuration
```systemctl daemon-reload```
