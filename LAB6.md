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

## Part 4
Ik heb een script gemaakt dat van de de volgende stappen uitvoert op alle switches:
- "show ip interface brief". De output wordt weggeschreven in een bestand (met w, waardoor oude content van het bestand verwijderd word)
- Het bestand wordt uitgelezen. 1 voor 1 word nagekeken of de interface vlan of port-channel is. Indien dit niet het geval is word nagekeken of de port down is.
- Indien de port "down" is word die uitgezet. Er wordt ook een beschrijving meegegeven en de port wordt in een niet-bestaande vlan gestoken.
```python
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

    
def getNetworkPorts(networkDevice,ip):
    print("show ip interface brief of device {}".format(networkDevice))
    sshCli = connect(ip)
    output = sshCli.send_command("show ip interface brief")
    sshCli.disconnect()
    return output

def checkPort(ip,port,status):
    if port.startswith('Vlan') == False or port.startswith('Port-channel') == False:
        if status == 'down':
            print("Port {} of device {} is down".format(port,ip))
            sshCli = connect(ip)
            
            commands = ['interface {}'.format(port), 'descri shut down by netmiko','shut','switchport mode access','switchport access vlan 456']
            sshCli.send_config_set(commands)
            sshCli.disconnect()


networkDevices = {'Switch1':'172.17.6.4', 'Switch2':'172.17.6.5', 'Switch3':'172.17.6.6', }
for device, ip in networkDevices.items():
    

    portList = getNetworkPorts(device,ip)
    f = open('portList.txt',"w")
    f.write(portList)
    f.close()

    file = open('portList.txt','r')
    lines = file.readlines()
    count = len(lines)
    for i in range(1,count):
        lijn = lines[i]
        port = lijn.split()
        checkPort(ip,port[0],port[4])

    file.close()

```

## Problemen
Veel problemen heb ik niet gehad. Buiten bij het Part 4, daar heb ik moeten zoeken hoe ik de output van "show ip interface brief" kon gebruiken als input voor een ander commando. Ik kon niet lijn per lijn de output afprinten, waardoor ik eerst heb moeten wegschrijven naar een file.

Blijkbaar kan je een bestand niet lezen als je die hebt geöpend met "w".
```python
f = open('portList.txt','w')
```
Daardoor moest ik eerst het bestand sluiten, om daarna terug te openen met "r".
 ```python
 file = open('portList.txt','r')
 ```

 Ik wou ook niet telkens alle poorten van een switch veranderen, daarom heb ik een bestand test.py aangemaakt. Met dat script kon ik gemakkellijk kleine onderdelen testen.