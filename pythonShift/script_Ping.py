import os
ipl = ['8.8.8.8','8.8.4.4','192.168.0.1']

for ip in ipl:
    response = os.popen('ping -c 4 ' + ip).read()
    if '4 recebidos' in response:
        print(ip,' está UP')
    else:
        print(ip, ' está DOWN')
