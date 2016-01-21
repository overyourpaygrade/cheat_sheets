###### how the overall status of NetworkManager
```nmcli general status```

###### control NetworkManager logging
```nmcli general logging```

###### show all connections
```nmcli connection show```

###### show active connections
```nmcli connection show --[a]ctive```

###### show devices recognized by network manager and their state
```nmcli device status```

###### start or stop any network interface
```
nmcli con up id bond0
nmcli dev disconnect iface bond0
```

