##### IP queries

###### addr - Display IP addresses and property information (abbrv of address)

###### Show info on all addresses
`ip addr`

###### Show info of one device
`ip addr show dev eth0`

###### link - Manage and display the state of all network interfaces

###### show info for all interfaces
`ip link`

###### Display info for one device
`ip link show dev eth0`

###### Display interface statistics
`ip -s link`

###### route - display and alter the routing table

###### List all of the route entries in the kernel
`ip route`

###### maddr - Manage and display multicast IP addresses

###### Manage and display multicast IP addresses
`ip maddr`

###### Display multicast information for device eth0
`ip maddr show dev eth0`

###### neigh - Show neighbor objects; also known as the ARP table for IPv4

###### Display neighbour objects
`ip neigh`

###### Show the ARP cache for device eth0
`ip neigh show dev eth0`

###### help = Display a list of commands and arguments for each subcommand

###### Display ip commands and arguments
`ip help`

###### Display address commands and arguments
`ip addr help`

###### Display link commands and arguments
`ip link help`

###### Display neighbour commands and arguments
`ip neigh help`

---------

##### Multicast addressing

###### maddr add - Add a static link-layer multicast address
`ip maddr add 33:33:00:00:00:01 dev eth0` 

###### maddr del - Delete a multicast address
`ip maddr del 33:33:00:00:01 dev eth0`

---------

##### Modifying address and link properties

###### addr add - Add an address
`ip addr add 192.168.1.1/24 dev eth0`

###### addr del - Delete an address
`ip addr del 192.168.1.1/24 dev eth0`

###### link set - Alter the status of the interface

###### Bring eth0 online
`ip link set eth0 up`

###### Bring eth0 offline
`ip link set eth0 down`

###### Set the MTU on eth0 to 9000
`ip link set eth0 mtu 9000`

###### Enable promiscuous mode for eth0
`ip link set eth0 promisc on`

---------

##### Adjusting and viewing routes

###### route add - Add an entry to the routing table

###### Default route for all via local gateway
`ip route add default via 192.168.1.1 dev eth0`

###### Add a route to the 192.168.1.0/24 via gw
`ip route add 192.168.1.0/24 via 192.168.1.1`

###### Add route to 192.168.1.0/24 that can be reached on dev eth0
`ip route add 192.168.1.0/24 dev eth0`

###### route delete - Delete a routing table entry

###### Delete a routing table entry
`ip route delete 192.168.1.0/24 via 192.168.1.1`

###### route replace - Replace, or add if not defined, a route

###### Replace the defined route for 192.168.1.0/24 to use device eth0
`ip route replace 192.168.1.0/24 dev eth0`

###### route get - Display the route an address will take

###### Display the route taken for IP 192.168.1.5
`ip route get 192.168.1.5`

