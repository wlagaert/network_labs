# LAB 7 - YANG, NETCONFIG and RESTCONFIG
## 7.1 Install CRS1000v VM
Cisco DEVNET 7.0.3
### 7.1.1 Install the CRS1000v on VirtualBox
De iso en ova-files werden gedownload. Ik heb de ova geïmporteerd in Virtualbox, daarna heb ik in de eerste cd-rom van CRS1000v VM de iso-file gelaad.

#### Problemen
Ik ben een paar problemen tegengekomen bij de stap om een ip-adres te krijgen van de dhcp-server VirtualBox.

Ik moest "Cable Connect" aanvinken en ik heb ook Promiscuous mode op "allow all" gezet in de internetsettings van de VM. 

Daarna kreeg hij wel een ip-adres.

### 7.1.2 Verify Communications to CRS1000v VM
#### Ping
Ik heb de DEVASC-vm opgestart. Daarna heb ik een ping gedaan naar het adres dat CRS1000v zonet gekregen heeft.

#### SSH

In een terminal heb ik een ssh sessie gestart naar 'CRS1000v'  met als gebruiker 'cisco' en paswoord 'cisco213!'. Na controle dat dat lukte heb ik de sessie beëindigd met 'exit'

#### https
Via een browser op zowel DEVASC als mijn Windows 11 naar 'HTTP://192.168.65.101' gegaan. De waarschuwingen kan je negeren om uiteindelijk op de inlogpagina te komen.

Daarna opnieuw inloggen met login en paswoord om te controleren dat het lukte.

#### Problemen
- De ethernetsettings van DEVASC stonden nog fout doordat ik deze op bridged mode had gezet voor LAB 6

## 7.2 Explore YANG Models
Cisco DEVNET 8.3.5
### Launch DEVASC VM

De vm werd opgestart.

### Explore a YANG Model on github

Via een browser werd een yang-bestand bekeken. Onder de list 'interface' (die in de container 'interfaces' zit) zien we een leaf 'Enabled'. Dit is een boolean.

Ik maak een map aan en daarin download ik m.b.v. wget de yang-file. 

```shell
# controle om te zien of pyang geïnstalleerd is
pyang -v

#indien het niet geïnstalleerd is:
pip3 install pyang --upgrade

```

Met behulp van 'pyang -h | more' krijgen we meer informatie over pyang. We zien dat we met '-f' het formaat kunnen veranderen naar bijvoorbeeld tree. We doen dit op de gedownloade file
 ```shell
 pyang -f tree ietf-interfaces.yang
 ```

 Nu is de file veel duidelijker om te lezen. We vinden veel sneller de leaf 'enabled' terug.

#### Problemen

Ik had niet de raw file gedownload, maar de http-pagina waardoor het commande 'pyang -f tree ietf-interfaces.yang' niet werktte. Na het verwijderen van de foute file en het downloaden van de juiste werkte het wel.

## 7.3 Use NETCONFT to access an IOS XE Device
Cisco DEVNET 8.3.6

### Part 1
Werd reeds gedaan in LAB 7.1

### Part 2

We moeten controleren of de NETCONF SSh daemon gestart is. Dit doen we door op de switch (via ssh) het commando 'show platform software yang-management process' uit te voeren. Dan kunnen we zien of die daemon aan staat. Indien die uit staat:

```shell
conf t
netconf-yang
```

Daarna moeten we de ssh-sessie sluiten omdat we een andere ssh-sessie moeten opstarten naar die daemon.

```shell
ssh cisco@192.168.56.101 -p 830 -s netconf
# 830 = poort
# netconf = subsystem
```

We krijgen dan een hallo-bericht van de andere VM. Dit moeten we beantwoorden met een eigen hallo bericht, anders wordt de sessie beëindigd.
```xml
<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<capabilities>
<capability>urn:ietf:params:netconf:base:1.0</capability>
</capabilities>
</hello>
]]>]]>
```
']]>]]>' is het einde van het bericht.

Op de router kunnen we dan m.b.v. 'show netconf-yang sessions' de actieve sessie zien.

We kunnen verschillende dingen doen met deze ssh d.m.v. Remote Procedure Call messages. Wij vragen een xml op met de informatie over de interfaces. Dit doen we met het volgende bericht:
```xml
<rpc message-id="103" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<get>
<filter>
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
</filter>
</get>
</rpc>
]]>]]>
```

Daarna krijgen we de xml binnen met op het einde weer die ']]>]]>'. Deze kunnen we online mooier maken met een 'xml prettify'.

![](images/7-1.png)

Om de sessie te sluiten:
```xml
<rpc message-id="9999999" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<close-session />
</rpc>
```

Op de router zien we dat er geen actieve sessies meer zijn.

### Part 3 - Eerste script
Eerst controleren we of ncclient geïnstalleerd is
```shell
pip3 list --format=columns | grep ncclient
```

We maken een script aan met de volgende code om alle mogelijkheden te zien:
```python
from ncclient import manager
import xml.dom.minidom

m = manager.connect (
    host="192.168.56.101",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)

#Hiermee printen we alle mogelijkheden af

print('#Supported Capabilities (YANG models):')
for capability in m.server_capabilities:
    print(capability)
```
We kunnen de laatste 3 regels in commentaar zetten en daarna het scrpt runnen om te zien of de connectie werkt.


### Part 4 - Configuratie ophalen
We zetten de laatste 3 regels in commentaar aangezien we dit nu niet meer nodig hebben. We voegen daarna de volgende code toe:

```python
#hiermee krijgen we de running config
netconf_reply = m.get_config(source = "running")
#Bij deze print heel de xml achter elkaar, zonder nieuwe regels of enters
print(netconf_reply)

#mooier afeprint (import xml.dom.minidom)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
```
Als we het script runnen met enkel de mooie print krijgen we het volgende resultaat:
![](images/7-2.png)

Nu krijgen we nog alle yang models. We kunnen een filter gebruiken om enkel een specifiek model te krijgen. 'netconf_reply' wordt aangepast om deze filter te gebruiken.
```python
#aanmaken van een variabele filter om een specifiek YANG model te gebruiken.
netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""

#hiermee krijgen we de running config
netconf_reply = m.get_config(source = "running", filter = netconf_filter)
```

### Part 5

We kunnen netconf_reply en de prints in commentaar zetten aangezien we die niet meer nodig hebben.

Er wordt een nieuwe variabele aangemaakt om de hostname van de router te veranderen. Daarna wordt deze gebruikt om de configuratie aan te passen met edit_config()
```python
#aanmaken van een config variabele om de configuratie van een apparaat te wijzigen
netconf_hostname = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>NEWHOSTNAMEWL</hostname>
    </native>
</config>
"""
#configuratie aanpassen en resultaat mooi printen
netconf_reply = m.edit_config(target="running", config=netconf_hostname)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
```

Het aanmaken van een eerste loopback interface
```python
print("Aanmaken loopback interface")
print("---------------------------")

#aanmaken loopback config variabele
netconf_loopback = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>1</name>
                <description>My first NETCONF loopback</description>
                <ip>
                    <address>
                        <primary>
                            <address>10.1.1.1</address>
                            <mask>255.255.255.0</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
```
Op de switch zien we nu de nieuwe loopback interface
![](images/7-3.png)

Nu gaan we een 2e loopback interface aanmaken met hetzelfde ip-adress. We gaan het resultaat niet printen. 
```python
netconf_newloop = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>2</name>
                <description>My first second loopback</description>
                <ip>
                    <address>
                        <primary>
                            <address>10.1.1.1</address>
                            <mask>255.255.255.0</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_newloop)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
```
Normaal gezien gaan we wel een foutmelding krijgen dat niet alle commando's uitgevoerd kunnen worden. (2 interfaces met hetzelfde ip-adres)

![](images/7-4.png)

#### Problemen
bij het aanmaken van de 2e loopback interface had ik enkel de description aangepast, niet naam van de interface.

### Part 6 - Pas het script aan

Ik heb besloten om de description van de interface GigabitEthernet1 aan te passen. Ik doe dit met de volgende code:
```python
netconf_changedescription = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <GigabitEthernet>
                <name>1</name>
                <description>GigabitEthernet1 port - the description was VBox</description>
            </GigabitEthernet>
        </interface>
    </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_changedescription)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
```

Na het uitvoeren krijg ik dit resultaat in de running config van de router:
![](images/7-5.png)

## 7.4 - Use RESTCONF to access an IOS XE Device
Cisco DEVNET 8.3.7
