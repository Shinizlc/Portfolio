import paramiko
from pprint import pprint
from time import sleep
hosts=['sjc01-c01-ldb20','sjc01-c01-ldb21','sjc01-c01-ldb22','sjc01-c01-ldb23','sjc01-c01-ldb24','sjc01-c01-ldb25','sjc01-c01-ldb31','sjc01-c01-ldb32',
'sjc01-c01-ldb33','sjc01-c01-ldb37','sjc01-c01-ldb38','sjc01-c01-ldb39','sjc01-c01-ldb34','sjc01-c01-ldb35','sjc01-c01-ldb36',
'sjc01-c01-ldb40','sjc01-c01-ldb41','sjc01-c01-ldb42','sjc01-c01-ldb43',
'sjc01-c01-ldb44','sjc01-c01-ldb45','sjc01-c01-ldb46','sjc01-c01-ldb47','sjc01-c01-ldb48']
# hosts=['iad41-c01-ldb01','iad41-c01-ldb02','iad41-c01-ldb03',
# 'iad41-c01-ldb04','iad41-c01-ldb05','iad41-c01-ldb06','iad41-c01-ldb07','iad41-c01-ldb08','iad41-c01-ldb09',
# 'iad41-c01-ldb10','iad41-c01-ldb11','iad41-c01-ldb12','iad41-c01-ldb13','iad41-c01-ldb14','iad41-c01-ldb15',
# 'iad41-c01-ldb16','iad41-c01-ldb17','iad41-c01-ldb18','iad41-c01-ldb19','iad41-c01-ldb20','iad41-c01-ldb21','iad41-c01-ldb22','iad41-c01-ldb23','iad41-c01-ldb24']
command='df -h | grep -i data'



paramiko_client = paramiko.SSHClient()
paramiko_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for host in hosts:
    try:
        paramiko_client.connect(host, password='Px2h69tuPNEuPwyQ', username='Aleksei.Semerikov')
        stdin,stdout,stderr = paramiko_client.exec_command(command)
        pprint('#############################################')
        pprint(f'The command "{command}" was executed on {host} host')
        for line in stdout.readlines():
            pprint(line.strip())
        sleep(5)
    except:
        print(f'error in {host}')
        sleep(5)



