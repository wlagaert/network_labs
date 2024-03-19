# LAB 3
## Part 1: Python Programming Review
Cisco DEVNET 1.3.3

Dit hadden we reeds gedaan en moesten we niet documenteren.

## Part 2: Explore Python Development Tools
Cisco DEVNET 3.1.12
### 3.2.1 

Launch the DEVASC VM

### 3.2.2

**De python installatie nakijken**

```bash
devasc@labvm:~$ python3 --version
Python 3.8.2
devasc@labvm:~$ which python3
/usr/bin/python3
```

### 3.2.3
**PIP en virtuele omgeving**


Er wordt een python virtuele omgeving aangemaakt om te voorkomen dat er problemen komen door verschillende packages die geïnstalleerd zijn. In een virtuele omgeving weten we welke packages geïnstalleerd zijn en ligt de python-versie ook vast. Daardoor is het veel consistenter dan bij de normale omgeving.

Het aanmaken van een virtuele omgeving gebeurd d.m.v. de venv tool

```bash
devasc@labvm:~$ cd labs/devnet-src/python
devasc@labvm:~/labs/devnet-src/python$ ls
devices.txt  file-access-input.py  file-access.py  hello-world.py  if-acl.py  if-vlan.py  personal-info.py
devasc@labvm:~/labs/devnet-src/python$ python3 -m venv devfun
devasc@labvm:~/labs/devnet-src/python$
```

Daarna wordt de virtuele python omgeving geactiveerd en getest. Met 'pip3 freeze' controleren we welke packages er geïnstalleerd zijn. 

```bash
devasc@labvm:~/labs/devnet-src/python$ ls
devfun  devices.txt  file-access-input.py  file-access.py  hello-world.py  if-acl.py  if-vlan.py  personal-info.py
devasc@labvm:~/labs/devnet-src/python$ source devfun/bin/activate
(devfun) devasc@labvm:~/labs/devnet-src/python$ pip3 freeze
(devfun) devasc@labvm:~/labs/devnet-src/python$ pip3 install requests
Collecting requests
  Downloading requests-2.31.0-py3-none-any.whl (62 kB)
     |████████████████████████████████| 62 kB 627 kB/s 
Collecting certifi>=2017.4.17
  Downloading certifi-2024.2.2-py3-none-any.whl (163 kB)
     |████████████████████████████████| 163 kB 3.0 MB/s 
Collecting urllib3<3,>=1.21.1
  Downloading urllib3-2.2.1-py3-none-any.whl (121 kB)
     |████████████████████████████████| 121 kB 14.3 MB/s 
Collecting charset-normalizer<4,>=2
  Downloading charset_normalizer-3.3.2-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (141 kB)
     |████████████████████████████████| 141 kB 22.6 MB/s 
Collecting idna<4,>=2.5
  Downloading idna-3.6-py3-none-any.whl (61 kB)
     |████████████████████████████████| 61 kB 366 kB/s 
Installing collected packages: certifi, urllib3, charset-normalizer, idna, requests
Successfully installed certifi-2024.2.2 charset-normalizer-3.3.2 idna-3.6 requests-2.31.0 urllib3-2.2.1
(devfun) devasc@labvm:~/labs/devnet-src/python$ pip3 freeze
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.2.1

```
Wanneer je in de virtuele omgeving zijt zie je vooran (devnet). Om uit de virtuele omgeving te gaan moet je deze deactiveren. 

```bash
(devfun) devasc@labvm:~/labs/devnet-src/python$ deactivate
devasc@labvm:~/labs/devnet-src/python$ 
```

Nu kunnen we controleren welke packages er geïnstalleerd zijn in de algemene (niet virtuele) omgeving.

```bash
devasc@labvm:~$ python3 -m pip freeze
aiohttp==3.6.2
ansible==2.9.9
apache-libcloud==2.8.0
appdirs==1.4.3
apturl==0.5.2
.....
```

Ze kunnen gebruik maken van grep om snel te kijken welke versie van een package geïnstalleerd is. Ook kunnen we zo snel zien of een package wel geïnstalleerd is.

```bash
devasc@labvm:~$ python3 -m pip freeze | grep requests
requests==2.22.0
requests-kerberos==0.12.0
requests-ntlm==1.1.0
requests-toolbelt==0.9.1
requests-unixsocket==0.2.0
```

### 3.2.4
**De virtuele omgeving delen**

Dit wordt gedaan door de geïnstalleerde packages uit de virtuele omegving weg te schrijven in een txt-bestand. Dit bestand kan dan worden gebruikt in een 2e virtuele omgeving om de packages te installeren.

```bash
devasc@labvm:~$ cd labs/devnet-src/python/
devasc@labvm:~/labs/devnet-src/python$ source devfun/bin/activate
(devfun) devasc@labvm:~/labs/devnet-src/python$ pip3 freeze > requirements.txt
(devfun) devasc@labvm:~/labs/devnet-src/python$ deactivate
devasc@labvm:~/labs/devnet-src/python$ ls -l
total 36
drwxrwxr-x 6 devasc devasc 4096 Mar 19 09:46 devfun
-rw-r--r-- 1 devasc devasc  419 Feb 20 18:40 devices.txt
-rw-rw-r-- 1 devasc devasc  198 Feb 20 18:39 file-access-input.py
-rw-rw-r-- 1 devasc devasc   99 Feb 20 18:28 file-access.py
-rw-rw-r-- 1 devasc devasc   20 Feb 20 17:47 hello-world.py
-rw-rw-r-- 1 devasc devasc  328 Feb 20 18:20 if-acl.py
-rw-rw-r-- 1 devasc devasc  188 Feb 20 18:13 if-vlan.py
-rw-rw-r-- 1 devasc devasc  279 Feb 20 18:11 personal-info.py
-rw-rw-r-- 1 devasc devasc   86 Mar 19 10:11 requirements.tx
```
Daarna wordt een nieuwe virtuele omgeving aangemaakt. Vervolgens wordt van het tekst-bestand gebruik gemaakt voor de installatie van de packages.
```bash
devasc@labvm:~/labs/devnet-src/python$ python3 -m venv devnew
devasc@labvm:~/labs/devnet-src/python$ source devnew/bin/activate
(devnew) devasc@labvm:~/labs/devnet-src/python$ pip3 install -r requirements.txt 
Collecting certifi==2024.2.2
  Using cached certifi-2024.2.2-py3-none-any.whl (163 kB)
Collecting charset-normalizer==3.3.2
  Using cached charset_normalizer-3.3.2-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (141 kB)
Collecting idna==3.6
  Using cached idna-3.6-py3-none-any.whl (61 kB)
Collecting requests==2.31.0
  Using cached requests-2.31.0-py3-none-any.whl (62 kB)
Collecting urllib3==2.2.1
  Using cached urllib3-2.2.1-py3-none-any.whl (121 kB)
Installing collected packages: certifi, charset-normalizer, idna, urllib3, requests
Successfully installed certifi-2024.2.2 charset-normalizer-3.3.2 idna-3.6 requests-2.31.0 urllib3-2.2.1
#Nu wordt nagekeken of de packages effectief geïnstalleerd werden:
(devnew) devasc@labvm:~/labs/devnet-src/python$ pip3 freeze
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.2.1
#Ten slotten deactiveren we de omgeving.
(devnew) devasc@labvm:~/labs/devnet-src/python$ deactivate
```

## Part 3: Explore Python Classes
Cisco DEVNET 3.4.6

### 3.3.1
Launch the DEVASC VM

### 3.3.2
**Het vershil tussen funcities, methoden en classes**

Functie:
Een codeblock die kan worden opgeroepen via een naam. Daardoor moeten stukken code niet telkens herhaald worden.

```python
def functienaam:
    print("Hello World")
# functie oproepen
functienaam()
```

Methode:
Een methode kan niet rechtstreeks opgeroepen worden. Eerst moet er een instantie van de class worden aangemaakt, waarna de methodes kunnen worden opgeroepen.

```python
class className
    def method1
        ...lots of code
    def method2
        ...even more code
    def method3
        ...guess what. Yep, more code

#instantie van de class. Dit is op hetzelfde niveau als de class.
myClass = className()

#daarna kunnen de methodes worden opgeroepen
myClass.method1()
myClass.method2()
myClass.method3()

```
### 3.3.3
**een functie aanmaken**

Nu gaan we zelf een functie schrijven en gebruiken. Eerst maken we een functie aan in een tekstbestand. In hetzelfde tekstbestand roepen we 3 keer de functie op.

De code van het tekst-bestand (myCity.py):
```python
def myCity(city):
	print("I live in " + city + ".")
myCity("Leuven")
myCity("Antwerpen")
myCity("Cannes")
```

Daarna wordt het uitgevoerd:
```bash
devasc@labvm:~/labs/devnet-src/python$ python3 myCity.py 
I live in Leuven.
I live in Antwerpen.
I live in Cannes.
```
### 3.3.4

Nu gaan we een class aanmaken en gebruiken. Eerst wordt er een tekstbestand myLocation.py aangemaakt met de volgende code
```python
class Location:
	def __init__(self, name, country):
		self.name = name
		self.country = country

	def myLocation(self):
		print("Hi, my name is " + self.name + " and I live in " + self.country + ".")
```
Als test wordt dit gestart om te kijken of er foutmeldingen zijn. Er is nog geen output, aangezien de class en method niet opgeroepen worden.

Onderaan myLocation.py gaan we nu een instantie maken van de class om vervolgens de method myLocation op te roepen.

```python
loc1 = Location("Thomas","Portugal")
loc1.myLocation()
```
De output van het programma nu:
```bash
devasc@labvm:~/labs/devnet-src/python$ python3 myLocation.py 
Hi, my name is Thomas and I live in Portugal.
```
We kunnen meerdere instanties oproepen? Elke instantie heeft zijn eigen meegeven waarden.
```python
loc2 = Location("Ying","China")
loc3 = Location("Amare","Kenya")
loc2.myLocation()
loc3.myLocation()
your_loc = Location("Wim","België")
your_loc.myLocation()
```

Nu is er extra output:
```bash
devasc@labvm:~/labs/devnet-src/python$ python3 myLocation.py 
Hi, my name is Thomas and I live in Portugal.
Hi, my name is Ying and I live in China.
Hi, my name is Amare and I live in Kenya.
Hi, my name is Wim and I live in België
```

#### Problemen
Ik had niet echt problemen. Buiten een schrijffout bij your_loc, waardoor ik iets oproep dat niet bestond.

### 3.3.5 
**circleClass.py**
 Eerst word de class Circle aangemaakt. Wanneer er een instantie van de class Cirlce wordt aangemaakt kunnen er gegevens worden meegeven. Dit gebeurd door middel van de __init__ method. De inhoud van de meegeven variabele (radius) wordt in een nieuwe variable (self.radius) weggeschreven. Hierdoor kunnen de andere methods ook aan deze data.

 ```python
 class Circle:
    def __init__(self, radius):
        self.radius = radius
 ```

 De 2e method van the Circle class berekend de omtrek. De waarde van pi wordt in de variabele pi weggeschreven. Daarna wordt de omtrek berekend (pi X straal X 2) en in de variable circumverenceValue weggeschreven. Tot slot wordt die waarde terug gestuurd.
 ```python
 def circumference(self):
        pi = 3.14
        circumferenceValue = pi * self.radius * 2
        return circumferenceValue
 ```

De 3e methode  dient om de omtrek van de cirkel af te printen. Eerst wordt de method circumference opgeroepen en in een variabele gestoken. Door de return van circumference wordt dus de omtrek van de cirkel in myCircumference weggeschreven. Daarna wordt er een print gedaan met de straal en omtrek van de cirkel.

```python
    def printCircumference(self):
        myCircumference = self.circumference()
        print ("Circumference of a circle with a radius of " + str(self.radius) + " is " + str(myCircumference))
```

Tot slot worden er instanties van de class Circle gemaakt. Telkens wordt de waarde van de straal meegeven. Daarna wordt de method printCircumference van de aangemaakte instantie opgeroepen, waardoor de straal en omtrek van de instantie geprint worden.
```python
circle1 = Circle(2)
circle1.printCircumference()
circle2 = Circle(5)
circle2.printCircumference()
circle3 = Circle(7)
circle3.printCircumference()
```