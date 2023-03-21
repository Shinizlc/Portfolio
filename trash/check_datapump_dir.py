import cx_Oracle
import paramiko
import os
class PUMPDIR:
    os.environ['PATH'] = '/Users/aleksei.semerikov/OracleClient/instantclient_12_2:/Users/aleksei.semerikov/OracleClient/instantclient_12_2:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/Library/Frameworks/Mono.framework/Versions/Current/Commands'
    os.environ['TNS_ADMIN'] = '/Users/aleksei.semerikov/OracleClient/instantclient_12_2/network'
    os.environ['ORACLE_HOME'] = '/Users/aleksei.semerikov/OracleClient/instantclient_12_2'

#     list_db = ['PRO-ADB011', 'PRO-ADB012','PRO-ADB021', 'PRO-ADB022','PRO-ADB031', 'PRO-ADB032','PRO-ADB041', 'PRO-ADB042','PRO-ADB051','PRO-ADB052',
# 'PRO-ADB061', 'PRO-ADB062','PRO-ADB071', 'PRO-ADB072','PRO-ADB081','PRO-ADB082','PRO-ADB091','PRO-ADB092','PRO-ADB101','PRO-ADB102','PRO-ADB111',
# 'PRO-ADB112','PRO-ADB121','PRO-ADB122','PRO-ADB131','PRO-ADB132','PRO-ADB141','PRO-ADB142','PRO-ADB151','PRO-ADB152','PRO-ADB161','PRO-ADB162',
# 'PRO-ADB171','PRO-ADB172','PRO-ADB191','PRO-ADB192','PRO-ADB201','PRO-ADB202','PRO-ADB211','PRO-ADB212','PRO-ADB231','PRO-ADB232','PRO-ADB241','PRO-ADB242']
#
#     list_hosts = ['sjc01-p01-adb01','iad01-p01-adb01','sjc01-p02-adb01','iad01-p02-adb01','sjc01-p03-adb01','iad01-p03-adb01','sjc01-p04-adb01','iad01-p04-adb01',
#                   'sjc01-p05-adb01','iad01-p05-adb01','sjc01-p06-adb01','iad01-p06-adb01','sjc01-p07-adb01','iad01-p07-adb01','sjc01-p08-adb01','iad01-p08-adb01','sjc01-p09-adb01',
#                   'iad01-p09-adb01','sjc01-p10-adb01','iad01-p10-adb01','sjc01-p11-adb01','iad01-p11-adb01','sjc01-p12-adb01','iad01-p12-adb01','sjc01-p13-adb01','iad01-p13-adb01',
#                   'sjc01-p14-adb01','iad01-p14-adb01','sjc01-p15-adb01','iad01-p15-adb01','sjc01-p16-adb01','iad01-p16-adb01','sjc01-p17-adb01','iad01-p17-adb01','sjc01-p19-adb01','iad41-p19-adb01',
#                   'aws70-p20-adb01','aws71-p20-adb01','pdx08-p21-adb01','pdx09-p21-adb01','sjc01-p23-adb01','iad41-p23-adb01','sjc01-p24-adb01','iad41-p24-adb01']

    list_db = ['PRO-ADB311', 'PRO-ADB312', 'PRO-ADB321', 'PRO-ADB322', 'PRO-ADB331', 'PRO-ADB332', 'PRO-ADB341',
            'PRO-ADB342', 'PRO-ADB351', 'PRO-ADB352', 'PRO-ADB361', 'PRO-ADB362']
    list_hosts = ['ams01-p31-adb01','zrh01-p31-adb01','ams01-p32-adb01','zrh01-p32-adb01','aws73-p33-adb01','aws74-p33-adb01','fra07-p34-adb01','fra08-p34-adb01','ams01-p35-adb01','fra01-p35-adb01','ams01-p36-adb01','fra01-p36-adb01']
    list_zipped  = zip(list_db,list_hosts)
###341&342 potential problems
    #
    def __init__(self):
        self.main_function()

    def check_pump_dir(self,db):
        connection = cx_Oracle.connect(user="system", password="euLagoon0102",
                                       dsn=db)
        cursor = connection.cursor()
        result = cursor.execute('select directory_path from dba_directories where directory_name=:dump_dir',dump_dir='DUMP_DIR1')
        for res in result:
            return res[0]

    def check_num_files(self,host,path):
        cmd = 'ls -la '+ str(path)+'/*.dmp* | wc -l'
        print(cmd)
        while True:
            try:
                client = paramiko.client.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(hostname=host,port=22,username='oracle',password='Sid0raEUobtained2209!')
                stdin, stdout, stderr = client.exec_command(cmd)
                for res in stdout:
                    return res
            except:
                pass



    def main_function(self):
            for db_host in self.list_zipped:
                path = self.check_pump_dir(db_host[0])
                print(db_host[1])
                print(self.check_num_files(db_host[1],path))




check1 = PUMPDIR()
# print(check1.check_num_files('iad01-p07-adb01','/EXPORT/adb072/'))