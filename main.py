import time
import nmap
import smtplib
from datadata import local_ip
from datadata import my_mac_address
from datadata import account
from datadata import pswd
from datadata import f_account
from datadata import server
from datadata import port
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

nm = nmap.PortScanner()

nm.scan(hosts=local_ip, arguments='-sP', sudo=True)

host_list = nm.all_hosts()

server = smtplib.SMTP(server, port)
server.starttls()
server.login(account, pswd)
message = MIMEMultipart()
body_msg = 'Este es un bot que te avisa cuando tu hijo esta en casa'

n = len(host_list)
for host in host_list:
        if  'mac' in nm[host]['addresses']:
                print(host+' : '+nm[host]['addresses']['mac'])
                if my_mac_address == nm[host]['addresses']['mac']:
                        print('Dispositivo encontrado, enviando correo:', my_mac_address)
                        message['From']=account
                        message['To']=f_account
                        message['Subject']= "YA LLEGUE A CASA"
                        message.attach(MIMEText(body_msg, 'plain'))
                        server.send_message(message)
                        #server.sendmail(account, f_account, "YA estoy en casa")
                        server.quit()
                        n = 123456


        n = n-1
        if n == 0:
                print('No estoy en casa')
                message['From']=account
                message['To']=f_account
                message['Subject']= "NO estoy en casa"
                message.attach(MIMEText(body_msg, 'plain'))
                server.send_message(message)
                #server.sendmail(account, f_account, "AUN NO llego a casa")
                server.quit()
        elif n == 123455:
                
                print('Ya estoy en casa, apagando programa...')
                time.sleep(5)
                quit()
                
