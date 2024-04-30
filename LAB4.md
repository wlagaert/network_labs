# LAB 4
Hieronder de configuraties van de switches. Ik heb ervoor gezorgd dat dit gekopiëerd en geplakt kan worden in switches zonder configuratie.
## Switch 1
```
hostname LAB-RA03-A01-SW1
vlan 61 
name Management
vlan 62
name Data_Users
vlan 63
name Voice_Users
vlan 64
name Reserved
vlan 99
name Native
exit
spanning-tree mode rapid-pvst
spanning-tree vlan 61 priority 0
spanning-tree vlan 62 priority 0
spanning-tree vlan 63 priority 0
spanning-tree vlan 64 priority 0

ip default-gateway 172.17.6.1


int range gig1/0/21-22
channel-group 1 mode desirable
switchport mode trunk

int range gig1/0/23-24
channel-group 2 mode desirable

int port-channel 1
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 61,62,63,64

int port-channel 2
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 61,62,63,64


int gig1/0/20
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 61,62,63,64

int vlan 61
ip address 172.17.6.4 255.255.255.240
exit

username cisco privilege 15 secret cisco
service password-encryption
banner motd "only authorized access is allowed"
ip domain name data.labnet.local
crypto key generate rsa modulus 2048
line vty 0 15
password cisco
login local
transport input ssh
exit

```
## Switch 2
```
hostname LAB-RA03-A01-SW2
vlan 61 
name Management
vlan 62
name Data_Users
vlan 63
name Voice_Users
vlan 64
name Reserved
vlan 99
name Native
exit
spanning-tree mode rapid-pvst
spanning-tree vlan 61 priority 4096
spanning-tree vlan 62 priority 4096
spanning-tree vlan 63 priority 4096
spanning-tree vlan 64 priority 4096

ip default-gateway 172.17.6.1

int range gig1/0/21-22
channel-group 1 mode desirable
int range gig1/0/23-24
channel-group 3 mode desirable


int port-channel 1
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 61,62,63,64

int port-channel 3
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 61,62,63,64

int gig1/0/20
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 61,62,63,64

int vlan 61
ip address 172.17.6.5 255.255.255.240
exit

username cisco privilege 15 secret cisco
service password-encryption
banner motd "only authorized access is allowed"
ip domain name data.labnet.local
crypto key generate rsa modulus 2048
line vty 0 15
password cisco
login local
transport input ssh
exit

```
## Switch 3
```
enable
conf t
hostname LAB-RA03-A01-SW3
vlan 61 
name Management
vlan 62
name Data_Users
vlan 63
name Voice_Users
vlan 64
name Reserved
vlan 99
name Native
exit
spanning-tree mode rapid-pvst
spanning-tree pathcost method long
spanning-tree vlan 61 priority 8192
spanning-tree vlan 62 priority 8192
spanning-tree vlan 63 priority 8192
spanning-tree vlan 64 priority 8192
ip default-gateway 172.17.6.1


interface gig 0/1
switchport mode access
switchport access vlan 62

int range Fa0/21-22
channel-group 2 mode desirable
int range Fa0/23-24
channel-group 3 mode desirable

int port-channel 2
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 61,62,63,64

int port-channel 3
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 61,62,63,64


int vlan 61
ip address 172.17.6.6 255.255.255.240
exit

username cisco privilege 15 secret cisco
service password-encryption
banner motd "only authorized access is allowed"
ip domain name data.labnet.local
crypto key generate rsa modulus 2048
line vty 0 15
password cisco
login local
transport input ssh
exit

```
## Router 1
```
hostname LAB-RA06-C01-R01

interface gig 0/0/0.61
encapsulation dot1q 61
ip address 172.17.6.2 255.255.255.240
standby 61 ip 172.17.6.1
standby 61 priority 150
standby 61 preempt


interface gig 0/0/0.62
encapsulation dot1q 62
ip address 172.17.6.18 255.255.255.240
standby 62 ip 172.17.6.17
standby 62 priority 150
standby 62 preempt
ip helper-address 10.199.64.66

interface gig 0/0/0.63
encapsulation dot1q 63
ip address 172.17.6.34 255.255.255.240
standby 63 ip 172.17.6.33
standby 63 priority 150
standby 63 preempt

interface gig 0/0/0.64
encapsulation dot1q 64
ip address 172.17.6.50 255.255.255.240
standby 64 ip 172.17.6.49
standby 64 priority 150
standby 64 preempt

interface gig 0/0/0.99
encapsulation dot1q 99 native

interface gig 0/0/0
no shut

interface gig 0/0/1
ip address 10.199.65.111 255.255.255.224
no shut
exit

ip route 0.0.0.0 0.0.0.0 10.199.65.100

username cisco privilege 15 secret cisco
service password-encryption
banner motd "only authorized access is allowed"
ip domain name data.labnet.local
crypto key generate rsa modulus 2048
line vty 0 15
password cisco
login local
transport input ssh
exit

```

## Router 2
```
hostname LAB-RA06-C01-R02

interface gig 0/0/0.61
encapsulation dot1q 61
ip address 172.17.6.3 255.255.255.240
standby 61 ip 172.17.6.1
standby 61 preempt


interface gig 0/0/0.62
encapsulation dot1q 62
ip address 172.17.6.19 255.255.255.240
standby 62 ip 172.17.6.17
standby 62 preempt
ip helper-address 10.199.64.66

interface gig 0/0/0.63
encapsulation dot1q 63
ip address 172.17.6.35 255.255.255.240
standby 63 ip 172.17.6.33
standby 63 preempt

interface gig 0/0/0.64
encapsulation dot1q 64
ip address 172.17.6.51 255.255.255.240
standby 64 ip 172.17.6.49
standby 64 preempt

interface gig 0/0/0.99
encapsulation dot1q 99 native

interface gig 0/0/0
no shut

interface gig 0/0/1
ip address 10.199.65.211 255.255.255.224
no shut
exit

ip route 0.0.0.0 0.0.0.0 10.199.65.100


username cisco privilege 15 secret cisco
service password-encryption
banner motd "only authorized access is allowed"
ip domain name data.labnet.local
crypto key generate rsa modulus 2048
line vty 0 15
password cisco
login local
transport input ssh
exit

```
## Problemen
Veel problemen ben ik niet tegengekomen. Enkel typfouten bij ip-adressen. Daardoor was bijvoorbeeld de 'default gateway' van de switches fout.

Ook heb ik 1 keer de foute poort gebruikt om mijn laptop op aan te sluiten.