from time import sleep
import os
import cx_Oracle
import smtplib
from datetime import date
import csv
import pandas as pd
class check_job_status:
    os.environ['PATH'] = '/u01/app/oracle/product/12.2.0/db/bin:/bin:/usr/bin:/home/oracle/bin:/u01/app/oracle/product/12.2.0/db/OPatchA'
    os.environ['TNS_ADMIN'] = '/u01/app/oracle/product/12.2.0/db/network'
    os.environ['ORACLE_HOME'] = '/u01/app/oracle/product/12.2.0/db'
    today= date.today()
    today = today.strftime("%d/%m/%Y")
    flag_file = '/Users/aleksei.semerikov/PycharmProjects/CHECK_SCHEDULER_JOB /send_today_flag'
    def __init__(self,instance):
        self.instance = instance
        self.connection = cx_Oracle.connect(user="zportal", password="Minas_13Lugrom",
                                       dsn=self.instance)

        self.cursor = self.connection.cursor()
        #self.main_part()
    def check_readonly_status(self)->bool:

        self.cursor.execute('''select zportal.getbuzmeparameter('read_only_mode') from dual''')
        for val in self.cursor:
            if int(val[0])==0:
                return False
            elif int(val[0])==1:
                return True
            else:
                return None

    def check_job_completed(self):

        self.cursor.execute('''select count(1) from user_scheduler_job_run_details where job_name=:job_name and to_date(trunc(actual_start_date))=trunc(sysdate)''',job_name="JOB$_MESSAGES_DELETE")
        for val in self.cursor:
            if int(val[0])==0:
                return False
            elif int(val[0])==1:
                return True
            else:
                return None

    def return_job_status(self):
        self.cursor.execute('''select status,actual_start_date,run_duration from user_scheduler_job_run_details where job_name=:job_name and to_date(trunc(actual_start_date))=trunc(sysdate)''',job_name="JOB$_MESSAGES_DELETE")
        for status,actual_start_date,run_duration_time in self.cursor:
            return (f'A status for "MESSAGES_DELETES" job in unit {self.instance} is {status},actual_start_date:{actual_start_date},run_duration_time:{run_duration_time}')



    def check_runinng_jobs(self):

        self.cursor.execute("select count(1) from user_scheduler_running_jobs where job_name=:jobname",jobname="JOB$_MESSAGES_DELETE")
        for val in self.cursor:
            if int(val[0])==0:
                return False
            elif int(val[0])==1:
                return True
            else:
                return None

    def get_set_flag(self,flag_val):
        if flag_val==0:
            with open(check_job_status.flag_file,'r') as flag:
                try:
                    reader = csv.reader(flag,delimiter=',',)
                    for line in reader:
                        if line[1] == self.instance:
                            return line[0]
                        else:
                            continue
                    return None
                except IndexError:
                    return None
        elif flag_val==2:
            with open(check_job_status.flag_file, 'a') as flag:
                writer = csv.writer(flag)
                writer.writerow([check_job_status.today,self.instance])

        else:
            file = pd.read_csv(check_job_status.flag_file,header=0)
            file.loc[file['Instance']==self.instance,"Date"] = check_job_status.today
            file.to_csv(check_job_status.flag_file,index=False)


    def send_mail(self,text):
        HOST = "localhost"
        SUBJECT = "Test email from Python"
        TO = ["aleksei.semerikov@ringcentral.com"]
        FROM = "aleksei.semerikov@ringcentral.com"
        #text = "Python 3.4 rules them all!"
        BODY = "\r\n".join((
            "From: %s" % FROM,
            "To: %s" % TO,
            "Subject: %s" % SUBJECT,
            "",
            text
        ))
        server = smtplib.SMTP(HOST)
        server.sendmail(FROM, [TO], BODY)
        server.quit()

    def main_part(self):
        if not self.check_readonly_status():
            print(f'A unit {self.instance} in read/write mode')
            if not self.check_job_completed() and self.check_runinng_jobs():
                self.send_mail('Job is still running')
                return (f'Job is still running')
            elif self.check_job_completed() and not self.check_runinng_jobs():
                # print(check_job_status.today)
                # print(self.get_set_flag(0))
                if self.get_set_flag(0)==check_job_status.today:
                    pass
                elif self.get_set_flag(0) is None:
                    self.get_set_flag(2)
                    self.send_mail(self.return_job_status())
                    return self.return_job_status()
                else:
                    self.get_set_flag(1)
                    self.send_mail(self.return_job_status())
                    return self.return_job_status()
            else:
                return (f'doing nothing')

        else:
            return (f'A unit {self.instance} is in read mode. Jobs is not running here')

list = ['ADB311','ADB312','ADB321','ADB322','ADB331','ADB332','ADB341',
        'ADB342','ADB351','ADB352','ADB361','ADB362']
# list=['ADB311']
# while True:
#     for ins in list:
#         check_ins = check_job_status(ins)
#         print(check_ins.main_part())
#     sleep(360)

if __name__ == '__main__':
    for ins in list:
        check_ins = check_job_status(ins)
        print(check_ins.main_part())
#     check_ins.send_mail('testtrtr')

# for ins in list:
#     check_ins = check_job_status(ins)
#     check_ins.get_set_flag(1)