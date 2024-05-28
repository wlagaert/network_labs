import json
import requests
requests.packages.urllib3.disable_warnings()

#url die wordt gebruikt voor de get request
api_url = "https://172.17.6.2/restconf/data/ietf-interfaces:interfaces/interface=Loopback2"


#variabele met de headers van het formaat dat geacepteerd word
headers = { "Accept": "application/yang-data+json",
           "Content-type":"application/yang-data+json"
           
           }
#variabele met login en paswoord
basicauth = ("cisco", "cisco")

#een python dictionary met de data die de nieuwe interface zal aanmaken
yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback2",
        "description": "My First RESTCONF loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "200.200.200.200",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
        }
}

#a variable to send te put request and store the response
resp = requests.put(api_url,data=json.dumps(yangConfig), auth=basicauth,headers=headers,verify=False)

#er wordt getest of de ressponse code goed is. Dan wordt het antwooord normaal afgeprint. Anders als error bericht.
if(resp.status_code >= 200 and resp.status_code <= 299) :
    print("STATUS OK: {}".format(resp.status_code))
else:
    print("ERROR. STATUS Code: {} \nError Message: {}".format(resp.status_code,resp.json()))