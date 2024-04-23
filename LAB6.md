# LAB 6
## PART 1
### Seding single show command
```python
print("Connecting via SSH => show interface status (brief)")
from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="172.17.6.6",
    port="22",
    username="cisco",
    password="cisco"
    )
output=sshCli.send_command("show ip interface brief")
print(output)
```
### Seding multiple show commands
```python
print("Connecting via SSH => show vlan and ssh")
from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="172.17.6.6",
    port="22",
    username="cisco",
    password="cisco"
    )
output=sshCli.send_command("show ssh")
print(output)
output=sshCli.send_command("show vlan")
print(output)
```

### send multiple configuration commands to a single device
Eerst maak ik een config.txt aan met hierin de veranderingen die moeten gebeuren
```
!
config t
!
int FastEthernet0/1
switchport mode access
switchport acces vlan 62
exit
!
int FastEthernet0/2
switchport mode access
switchport acces vlan 62
exit
!
```

Daarna maak ik een python script dat de veranderingen uitvoert.
```python
from netmiko import ConnectHandler

cisco_Switch = {
    "device_type": "cisco_ios",
    "host": "172.17.6.6",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco"}

with ConnectHandler(**cisco_Switch) as net_connect:
    
    net_connect.enable()
    output = net_connect.send_config_from_file('config.txt')

    print (output)
    net_connect.disconnect()
```

## PART 2

### Send show commands to multiple devices
```python
print("Connecting via SSH => show vlan and ssh")
from netmiko import ConnectHandler
def connect(ip):
    sshCli = ConnectHandler(
        device_type="cisco_ios",
        host=ip,
        port="22",
        username="cisco",
        password="cisco"
        )
    return sshCli
print("show vlan and ssh of switch 172.17.6.6")
sshCli = connect('172.17.6.6')
output=sshCli.send_command("show vlan")
print(output)
output=sshCli.send_command("show ssh")
print(output)
print("show vlan and ssh of switch 172.17.6.5")
sshCli = connect('172.17.6.5')
output=sshCli.send_command("show vlan")
print(output)
output=sshCli.send_command("show ssh")
print(output)
```

### Send configuration commands to multiple devices

De file config.txt werd aangepast. Eerst werkte het script niet omdat de interface op de 2 andere switches niet bestonden.

```
!
config t
!
int Gig1/0/1
switchport mode access
switchport acces vlan 62
exit
!
int Gig1/0/2
switchport mode access
switchport acces vlan 62
exit
!
```
Het script
```python
from netmiko import ConnectHandler

def switch(ip):

    netApparaat = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco"}
    return netApparaat

cisco_Switch = switch('172.17.6.5')
with ConnectHandler(**cisco_Switch) as net_connect:
    
    net_connect.enable()
    output = net_connect.send_config_from_file('config.txt')

    print (output)
    net_connect.disconnect()



cisco_Switch = switch('172.17.6.4')
with ConnectHandler(**cisco_Switch) as net_connect:
    
    net_connect.enable()
    output = net_connect.send_config_from_file('config.txt')

    print (output)
    net_connect.disconnect()

```

### Run show commands and save the output

Het script showInterfaces.py werd aangepast. De code die werd toegevoegd:
```python
f = open("output.txt","a")
f.write("Show vlan on 172.17.6.6\n")
f.write(output)

#op het einde werrd de file afgesloten
f.close()
```
### Backup the device configurations
Ik heb een nieuw python script aangemaakt. Daarna heb ik 5 lege bestanden aangemaakt waarin de config dan komt.
```python
print("Connecting via SSH => show vlan and ssh")
from netmiko import ConnectHandler
def connect(ip):
    sshCli = ConnectHandler(
        device_type="cisco_ios",
        host=ip,
        port="22",
        username="cisco",
        password="cisco"
        )
    return sshCli

def saveConfig(netDevice,file):
    print("saving running configuration of {} in file {}".format(netDevice,file))
    f = open(file,"a")
    sshCli = connect(netDevice)
    output=sshCli.send_command("show run")
    f.write(output)
    f.close

saveConfig('172.17.6.2',"router1Config.txt")
saveConfig('172.17.6.3',"router2Config.txt")
saveConfig('172.17.6.4',"switch1Config.txt")
saveConfig('172.17.6.5',"switch2Config.txt")
saveConfig('172.17.6.6',"switch3Config.txt")
```

### configure a subset of Interfaces
Dit werd reeds gedaan in de 3e opdracht van Part 1

### Send device configuration using an external file
Ook dit had ik reeds gedaan in de 3e opdracht van Part 1

### Connect using a Python Dictionary

Het script showInterfaces.py werd aangepast. Er werd een functie toegevoegd voor het afprinten van "Show vlan" en "Show ssh". Daarna werd een dictionary aangemaakt met alle divices en hun ip-adres. Vervolgens werd van de nieuwe functie gebruik gemaakt om van alle devices die commando's uit te voeren en af te printen.

```python
def showVlanSSH(networkDevice,ip):
    print("show vlan of device {}".format(networkDevice))
    sshCli = connect(ip)
    output = sshCli.send_command("show vlan")
    print(output)

    print("show ssh of device {}".format(networkDevice))
    sshCli = connect(ip)
    output = sshCli.send_command("show ssh")
    print(output)

networkDevices = {'Router1':'172.17.6.2', 'Router2':'172.17.6.3', 'Switch1':'172.17.6.4', 'Switch2':'172.17.6.5', 'Switch3':'172.17.6.6', }
for device, ip in networkDevices.items():
    showVlanSSH(device,ip)
```

### Execute a script with a Function or classes
Dit werd reeds gedaan in de eerdere oefeningen.

### Execute a script with statements (if,ifelse, else)

De functie showVlanSSH werd aangepast zodat "show vlan" enkel uitgevoerd word wanneer het networkDevice een switch is.

```python
def showVlanSSH(networkDevice,ip):
    if networkDevice > 'Switch':
        print("show vlan of device {}".format(networkDevice))
        sshCli = connect(ip)
        output = sshCli.send_command("show vlan")
        print(output)

    print("show ssh of device {}".format(networkDevice))
    sshCli = connect(ip)
    output = sshCli.send_command("show ssh")
    print(output)
```

## Part 3
idem als Part 2. Alle switches en routers werden gebruikt.