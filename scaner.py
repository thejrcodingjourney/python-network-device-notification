#CON ESTE SCRIPT PUEDES SABER LA DIRECCIÓN MAC DE TU DISPOSITIVO

import nmap

nm = nmap.PortScanner()

results = nm.scan(hosts='192.168.1.0-254', arguments='-sP', sudo=True)

print(results)
