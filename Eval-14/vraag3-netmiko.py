print("Connecting via SSH => show ip interfaces")
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
def showVlanSSH(networkDevice,ip):
    print("show ip interfaces of device {}".format(networkDevice))
    sshCli = connect(ip)
    output = sshCli.send_command("show ip interface")
    print(output)

networkDevices = {'Router1':'172.17.6.2', 'Router2':'172.17.6.3', 'Switch1':'172.17.6.4', 'Switch2':'172.17.6.5', 'Switch3':'172.17.6.6', }
for device, ip in networkDevices.items():
    showVlanSSH(device,ip)