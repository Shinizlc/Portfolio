from time import sleep
import os
import cx_Oracle
import smtplib
from datetime import date
class check_job_status:
    os.environ['PATH'] = '/Users/aleksei.semerikov/OracleClient/instantclient_12_2:/Users/aleksei.semerikov/OracleClient/instantclient_12_2:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/Library/Frameworks/Mono.framework/Versions/Current/Commands'
    os.environ['TNS_ADMIN'] = '/Users/aleksei.semerikov/OracleClient/instantclient_12_2/network'
    os.environ['ORACLE_HOME'] = '/Users/aleksei.semerikov/OracleClient/instantclient_12_2'
    today= date.today()
    today = today.strftime("%d/%m/%Y")
    def __init__(self,instance):
        self.instance = instance
        self.connection = cx_Oracle.connect(user="system", password="euLagoon2209",
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

        self.cursor.execute('''select count(1) from dba_scheduler_job_run_details where job_name=:job_name and to_date(trunc(actual_start_date))=trunc(sysdate)-1''',job_name="JOB$_MESSAGES_DELETE")
        for val in self.cursor:
            if int(val[0])==0:
                return False
            elif int(val[0])==1:
                return True
            else:
                return None

    def return_job_status(self):
        self.cursor.execute('''select status,actual_start_date,run_duration from dba_scheduler_job_run_details where job_name=:job_name and to_date(trunc(actual_start_date))=trunc(sysdate)-1''',job_name="JOB$_MESSAGES_DELETE")
        for status,actual_start_date,run_duration_time in self.cursor:
            return (f'A status for "MESSAGES_DELETES" job in unit {self.instance} is {status},actual_start_date:{actual_start_date},run_duration_time:{run_duration_time}')



    def check_runinng_jobs(self):

        self.cursor.execute("select count(1) from dba_scheduler_running_jobs where job_name=:jobname",jobname="JOB$_MESSAGES_DELETE")
        for val in self.cursor:
            if int(val[0])==0:
                return False
            elif int(val[0])==1:
                return True
            else:
                return None

    def get_set_flag(self,flag_val):
        if not flag_val:
            with open('/Users/aleksei.semerikov/PycharmProjects/CHECK_SCHEDULER_JOB /send_today_flag','r') as flag:
                res = flag.readline()
                return res
        else:
            with open('/Users/aleksei.semerikov/PycharmProjects/CHECK_SCHEDULER_JOB /send_today_flag', 'w') as flag:
                flag.write(check_job_status.today)





    def send_mail(self,text):
        SERVER = "localhost"
        FROM = "aleksei.semerikov@ringcentral.com"
        TO = ["aleksei.semerikov@ringcentral.com"]
        SUBJECT = "Job JOB$_MESSAGES_DELETE status"
        # TEXT = "This message was sent with Python's smtplib."

        message = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (FROM, ", ".join(TO), SUBJECT, text)

        server = smtplib.SMTP(SERVER)
        #server.set_debuglevel(3)
        server.sendmail(FROM, TO, message)
        server.quit()

    def main_part(self):
        if not self.check_readonly_status():
            print(f'A unit {self.instance} in read/write mode')
            if not self.check_job_completed() and self.check_runinng_jobs():
               #self.send_mail('Job is still running')
                return (f'Job is still running')
            elif self.check_job_completed() and not self.check_runinng_jobs():
                # print(check_job_status.today)
                # print(self.get_set_flag(0))
                if self.get_set_flag(0)==check_job_status.today:
                    pass
                else:
                    self.get_set_flag(1)
                    #self.send_mail(self.return_job_status())
                    return self.return_job_status()
            else:
                return (f'doing nothing')

        else:
            return (f'A unit {self.instance} is in read mode. Jobs is not running here')

# list = ['PRO-ADB311','PRO-ADB312','PRO-ADB321','PRO-ADB322','PRO-ADB331','PRO-ADB332','PRO-ADB341',
#         'PRO-ADB342','PRO-ADB351','PRO-ADB352','PRO-ADB361','PRO-ADB362']
list=['PRO-ADB312']
while True:
    for ins in list:
        check_ins = check_job_status(ins)
        print(check_ins.main_part())
    sleep(360)
# for ins in list:
#     check_ins = check_job_status(ins)
#     print(check_ins.get_set_flag(0))