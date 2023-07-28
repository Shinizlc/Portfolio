import paramiko
from pprint import pprint
from time import sleep
# hosts=['sjc01-c01-ldb20','sjc01-c01-ldb21','sjc01-c01-ldb22','sjc01-c01-ldb23','sjc01-c01-ldb24','sjc01-c01-ldb25','sjc01-c01-ldb31','sjc01-c01-ldb32',
# 'sjc01-c01-ldb33','sjc01-c01-ldb37','sjc01-c01-ldb38','sjc01-c01-ldb39','sjc01-c01-ldb34','sjc01-c01-ldb35','sjc01-c01-ldb36',
# 'sjc01-c01-ldb40','sjc01-c01-ldb41','sjc01-c01-ldb42','sjc01-c01-ldb43',
# 'sjc01-c01-ldb44','sjc01-c01-ldb45','sjc01-c01-ldb46','sjc01-c01-ldb47','sjc01-c01-ldb48']
# hosts=['iad41-c01-ldb01','iad41-c01-ldb02','iad41-c01-ldb03',
# 'iad41-c01-ldb04','iad41-c01-ldb05','iad41-c01-ldb06','iad41-c01-ldb07','iad41-c01-ldb08','iad41-c01-ldb09',
# 'iad41-c01-ldb10','iad41-c01-ldb11','iad41-c01-ldb12','iad41-c01-ldb13','iad41-c01-ldb14','iad41-c01-ldb15',
# 'iad41-c01-ldb16','iad41-c01-ldb17','iad41-c01-ldb18','iad41-c01-ldb19','iad41-c01-ldb20','iad41-c01-ldb21','iad41-c01-ldb22','iad41-c01-ldb23','iad41-c01-ldb24']
hosts = ['ams01-c01-lda01','aws70-c01-lda11','aws71-c01-lda11','aws73-c01-lda11','aws74-c01-lda11','fra01-c01-lda01',
         'fra01-c01-lda01','fra07-c01-lda11','fra08-c01-lda11','iad41-c01-lda01','iad41-c01-lda02','iad41-c01-lda03','iad41-c01-lda05','sjc01-c01-lda01',
         'sjc01-c01-lda04','sjc01-c01-lda12','sjc01-c01-lda13','syd05-c01-lda11']

# hosts = ['ams01-c01-lda01']
# hosts = ['ams01-p31-adb01','zrh01-p31-adb01','ams01-p32-adb01','zrh01-p32-adb01','aws73-p33-adb01','aws74-p33-adb01','fra07-p34-adb01','fra08-p34-adb01','ams01-p35-adb01','fra01-p35-adb01','ams01-p36-adb01','fra01-p36-adb01']
# hosts = ['sjc01-p01-adb01','iad01-p01-adb01','sjc01-p02-adb01','iad01-p02-adb01','sjc01-p03-adb01','iad01-p03-adb01','sjc01-p04-adb01','iad01-p04-adb01',
#                   'sjc01-p05-adb01','iad01-p05-adb01','sjc01-p06-adb01','iad01-p06-adb01','sjc01-p07-adb01','iad01-p07-adb01','sjc01-p08-adb01','iad01-p08-adb01','sjc01-p09-adb01',
#                   'iad01-p09-adb01','sjc01-p10-adb01','iad01-p10-adb01','sjc01-p11-adb01','iad01-p11-adb01','sjc01-p12-adb01','iad01-p12-adb01','sjc01-p13-adb01','iad01-p13-adb01',
#                   'sjc01-p14-adb01','iad01-p14-adb01','sjc01-p15-adb01','iad01-p15-adb01','sjc01-p16-adb01','iad01-p16-adb01','sjc01-p17-adb01','iad01-p17-adb01','sjc01-p19-adb01','iad41-p19-adb01',
#                   'aws70-p20-adb01','aws71-p20-adb01','pdx08-p21-adb01','pdx09-p21-adb01','sjc01-p23-adb01','iad41-p23-adb01','sjc01-p24-adb01','iad41-p24-adb01']
#

# command = 'crontab -l | grep -v ^# | grep -i "backup_base_meta.sh\|backup_arc.sh\|gg_state.sh\|gg_lag.sh\|gg_hb.sh\|dbalert.mon.sh\|tbs_free_space.sh\|backup_export.sh" |wc -l'
# command = 'crontab -l | grep -v ^# | grep -i "listener_high_water_mark.sh" |wc -l'
# command  =  'ls /var/log/ringcentral/lda | wc -l'


paramiko_client = paramiko.SSHClient()
paramiko_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for host in hosts:
    while True:
        try:
            paramiko_client.connect(hostname=host,port=22,username='Aleksei.Semerikov',password='CHaWr_2_5aD-')
            command = 'ls /var/log/ringcentral/lda | wc -l'
            stdin,stdout,stderr = paramiko_client.exec_command(command)
            pprint('#############################################')
            pprint(f'The command was executed on {host} host')
            for line in stdout.readlines():
                pprint(f'number of files in /var/log/ringcentral/lda is  {int(line.strip())}')
            command = 'head -n 1 /etc/swe-version'
            stdin,stdout,stderr = paramiko_client.exec_command(command)
            for line in stdout.readlines():
                pprint(line.strip())
                sleep(1)
            break
        except:
            sleep(1)



