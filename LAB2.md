# LAB 2 (4.5.5) 

## PART 1

### 1.1 

DEVASC VM opgestart


### 1.2 

Chromium opgestart en naar de site library.demo.local gesurft.

### 1.3 

Bovenaan is een link voor developers om meer te weten te komen over de API. Daarop geklikt.

### 1.4 

Op GET /books geklikt. Daaronder kan je opties veranderen. Bijvoorbeeld of je ook de isbn-nummers wilt, op wat je wil sorteren, van welke auteur je de boeken wilt krijgen.
Wanneer je op execute klikt krijg je ook het curl-commando en de "request URL" te zien dat hij gebruikt heeft.

### 1.5 

GET /books uitgevoerd met alle waarden op default. Ik kreeg een lijst van alle boeken. Als test heb ik de boolean aangezet om ook de isbn-nummers te krijgen.

### 1.6 

Ik heb het curl-commande gekopiëerd en uitgevoerd in een terminal. Ik kreeg hetzelfde resultaat als via de webpagina.
Als test heb ik het formaat veranderd van JSON naar YAML

### 1.7 

Onder GET /books de optie aangezet om de ISBN-nummers ook te krijgen. Ik heb gemerkt dat de CURL en "Request URL" veranderd zijn. "includeISBN=true" is aan beide toegevoegd.
Als test heb ik aan het vorige curl-commande van de terminal "?includeISBN=true" toegevoegd op het einde van de url. (voor de -H)

### 1.8 

Op de demo website terug naar de lijst met api's gegaan. Daar gekozen voor post /loginViaBasic. Er werd een username en paswoord gevraagd. Hiervoor heb ik cisco & Cisco123! gebruikt.

Ik kreeg een token: "token": "cisco|FRcOotZrZiP-_54NEa-VPUzwvLtRkvHZOX2vkoXmYRg"

Daarna bovenaan op authorize geklikt. Er werd een "value" gevraagd. Daar de api-key in geplakt & op Authorize geklikt. Ik kreeg de boodschap "Authorized". Ik kreeg ook de naam X-API-KEY.

### 1.9 

Ik heb ook POST /books geklikt. Hiermee kan je boeken toevoegen aan de database via de API. 
payload:
```json
{
  "id": 4,
  "title": "IPv6 Fundamentals",
  "author": "Rick Graziani"
}
```

Ik voerde dit uit en kreeg als code 200. De payload was ook te zien in de response body. Ook kreeg ik het volgende curl-commando:


```shell
curl -X POST "http://library.demo.local/api/v1/books" -H "accept: application/json" -H "X-API-KEY: cisco|FRcOotZrZiP-_54NEa-VPUzwvLtRkvHZOX2vkoXmYRg" -H "Content-Type: application/json" -d "{ \"id\": 4, \"title\": \"IPv6 Fundamentals\", \"author\": \"Rick Graziani\"}"
```

Bovenaan de payload veranderd naar:
```json
{
  "id": 5,
  "title": "31 Days Before Your CCNA Exam",
  "author": "Allan Johnson"
}
```
Terug op execute geklikt en kreeg weeral code 200.

Daarna naar de website gegaan om te zien of beide boeken toegevoegd zijn aan de lijst.

### 1.10 

Terugggegaan naar GET /books. Alles standaard gelaten (dus geen isbn-nummers)


```json
Response:
[
  {
    "id": 0,
    "title": "IP Routing Fundamentals",
    "author": "Mark A. Sportack"
  },
  {
    "id": 1,
    "title": "Python for Dummies",
    "author": "Stef Maruch Aahz Maruch"
  },
  {
    "id": 2,
    "title": "Linux for Networkers",
    "author": "Cisco Systems Inc."
  },
  {
    "id": 3,
    "title": "NetAcad: 20 Years Of Online-Learning",
    "author": "Cisco Systems Inc."
  },
  {
    "id": 4,
    "title": "IPv6 Fundamentals",
    "author": "Rick Graziani"
  },
  {
    "id": 5,
    "title": "31 Days Before Your CCNA Exam",
    "author": "Allan Johnson"
  }
]
```
### 1.11 

naar de GET /books/{id} gegaan. Hierbij is het verplicht om een id in te vullen. Als parameter heb ik 4 ingevuld en uitgevoerd.

Ik kreeg code 200.
Het curl commande dat ik kreeg was:
curl -X GET "http://library.demo.local/api/v1/books/4" -H "accept: application/json"

De gegevens van boek met id 4 stond in de response body.

### 1.12 

Ik ben naar DELETE/books{id} gegaan. Ook hier is de parameter verplicht. De parameter die ik heb meegegeven was 4.

Ik kreeg opnieuw code 200. 
```shell
Curl-commando: 
curl -X DELETE "http://library.demo.local/api/v1/books/4" -H "accept: application/json" -H "X-API-KEY: cisco|FRcOotZrZiP-_54NEa-VPUzwvLtRkvHZOX2vkoXmYRg"
```
De gegevens van boek met id 4 stond in de response body.

Op de site was boek 4 verdwenen uit de lijst (na een refresh)

### 1.13

Terug gegaan naar GET /books. Na uitvoering ook hier gemerkt dat book met id 4 niet meer in de lijst staat.




## PART 2
### 2.1 

postman gestart

### 2.2 

Ik heb niet ingelogd, maar gekozen voor "lightweight api client"
Standaard is er al een untitles request gestart. Links zie GET staan. Je kan dit veranderen naar de andere API operations (post,put,patch,delete, head & options). 

Op de site met de API's de Request URL gekopieerd en geplakt in postman
request url:
http://library.demo.local/api/v1/books

Na dit verzonden te hebben kreeg ik de lijst met boeken.

### 2.3 

Ik heb een nieuwe request geopend. GET werd veranderd naar POST. Op de site bij POST /loginViaBasic de request url gekopieerd.

http://library.demo.local/api/v1/loginViaBasic

Daaronder bij het tabblad "Authorization" gekozen voor "Basic Auth". Daarna username cisco en paswoord Cisco123! ingevuld. 

Op Send geklikt, waarna ik een token kreeg:
"token": "cisco|m5EosFPlq9NGjfgUR7-_XqXxBZ3EB8UJSMiM03wdm1M"

### 2.4 

Ik heb in postman een nieuwe request aangemaakt & GET veranderd naar POST. Dezelfde request url uit 2.2 werd gebruikt:
http://library.demo.local/api/v1/books

In het tabblad Authorization de Type veranderd naar API Key. Als Key gekozen voor X-API-KEY (zie part 1). Als value de token uit 2.3.

Daarna naar het tabblad Body gegaan. Als input gekozen voor 'raw'. Rechts "Text" veranderd naar "JSON". 
In het inputveld eronder:

```json
{
    "id": 4,
    "title": "IPv6 Fundamentals",
    "author": "Rick Graziani",
    "isbn": "978 158144778"
}
```
Aan de rechterkant kan je de response code zien. Bij mij was dit code 200.

### 2.5 

Ik ben terug naar de eerste request gegaan.(zie punt 2.2). Opnieuw op Send geklikt om de nieuwe lijst te krijgen. Het zopas aangemaakte boek met id 4 staat er tussen.

### 2.6 

Terug naar de site met de api's gegaan. Daar bij GET /books gekozen gekozen voor includeISBN = true. Bij sortBy gekozen voor "author". Dit uitgevoerd en de lijst gekregen met alle boeken incl. isbn-nummers. De lijst was gesorteerd op de naam van de auteur. De request url was veranderd naar:

http://library.demo.local/api/v1/books?includeISBN=true&sortBy=author


Om dit in postman te doen onder parameters:
```
Key: includeISBN
Value: true

Key: sortBy
Value: author
```

De keys worden automatisch toegevoegd aan de request url naast "GET".

De response code was 200. Als antwoord kreeg ik dezelfde lijst als op de site.



## PART 3
### 3.1 

VS code geopend. Daarna File --> open folder en navigeren naar ~/labs/devnet-src/school-library

### 3.2 

Links add100RandomBooks.py klikken. Daarna zie je de python-code.

Aan het begin zie je dat request en json worden geïmporteerd. Ook Faker (onderdeel van faker()) word geïmporteerd. 

Je kan zien wat dit allemaal kan doen. Hiervoor in een terminal het volgende doen:
python3
from faker import Faker
fake = Faker()

daarna fake. typen en 2 keer op tab klikken. Nu zie je alles wat je met Faker kan doen. Het maakt een hele hoop random (valse) data aan.

Het script gebruikt:
fake.catch_phrase
fake.isbn13
fake.name
### 3.3

```python
Als test in dezelfde terminal:
print('My name is {}.'.format(fake.name()))
```

```python
Om de 3 methods te testen het volgende uitvoeren:
print('My name is {0} and I wrote "{1}" ({2}).'.format(fake.name(),fake.catch_phrase(), fake.isbn13()))
```

Je kan dit ook in een loop doen:
```python
for i in range(10):
	print(fake.name())
```

### 3.4 

Er zijn 2 functies. Zij gebruiken 3 variabelen:
- .APIHOST
- LOGIN
- PASSWORD

### 3.5 

de functie getAuthToken():
In de variabele authCreds worden login en paswoord gestoken.

Daarna word er een POST gestart:
```python
r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic", 
        auth = authCreds
    )
```
Aan de standaard url word /api/v1/loginViaBasic toegevoegd. Er word gebruik gemaakt van een f-string. De authCreds worden ook meegegeven.

Als r.status_code 200 is word het token gereturned, anders word er een Exception gethrowd.
```python
if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")
```
### 3.6 

de functie addBook:
Bij het oproepen van deze functie kunnen 2 variabelen worden meegegeven.
book
apiKey

Daarna word er net zoals bij getAuthToken een post gestart:
```python
    r = requests.post(
        f"{APIHOST}/api/v1/books", 
        headers = {
            "Content-type": "application/json",
            "X-API-Key": apiKey
            },
        data = json.dumps(book)
    )
    if r.status_code == 200:
        print(f"Book {book} added.")
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to add book
```
net zoals bij getAuthtoken word de status code gecontroleerd.

 ### 3.7 

het oproepen van de 2 functies:

de api key word opgevraagd en in de variabele apiKey gestoken:
apiKey = getAuthToken()

de faker module gebruiken voor het aanmaken van de valse boeken:
```python
for i in range(4, 105):
    fakeTitle = fake.catch_phrase()
    fakeAuthor = fake.name()
    fakeISBN = fake.isbn13()
    book = {"id":i, "title": fakeTitle, "author": fakeAuthor, "isbn": fakeISBN}
    # add the new random "fake" book using the API
    addBook(book, apiKey) 
```
Eerst worden de valse Title, Auteur en ISBN aangemaakt en in de variabele book gestoken.
 variabelen book & apiKey meegeven. 

Daarna word addBook gestart en worden de
for i in range(4,105) is een loop. Hij gaat hier dus 101 keer door.

### 3.8 

het programma runnen
```shell
cd ~/labs/devnet-src/school-library
python3 add100RandomBooks.py
```
In de browser terug naar de site van de library gegaan. Na een refresh zie ik de eersete pagina met 10 boeken. De boeken met id 4 en 5 bestonden reeds. Hier heeft hij de data overschreven met die fake data.

Via de api krijg je enkel de eerste 10 boeken. Je kan de page parameter gebruiken om de andere pagina's met boeken te zien
```shell
curl voor pagina 2:

curl -X GET "http://library.demo.local/api/v1/books?includeISBN=true&sortBy=id&page=2" -H "accept: application/json"
```
	












