from time import sleep
import os
import cx_Oracle
import smtplib
from datetime import date
import csv
import pandas as pd
from logging_module import logger
import csv
class check_job_status:
    os.environ['PATH'] = '/Users/aleksei.semerikov/OracleClient/instantclient_12_2'
    os.environ['TNS_ADMIN'] = '/Users/aleksei.semerikov/OracleClient/instantclient_12_2/network'
    os.environ['ORACLE_HOME'] = '/Users/aleksei.semerikov/OracleClient/instantclient_12_2'
    today= date.today()
    today = today.strftime("%d/%m/%Y")
    flag_file = '/Users/aleksei.semerikov/PycharmProjects/CHECK_SCHEDULER_JOB /send_today_flag'
    def __init__(self,instance):
        self.job_list = ['JOB$_RUNGARBAGE','JOB$_MESSAGES_DELETE']
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

    def check_job_completed(self,job_name):

        self.cursor.execute('''select count(1) from user_scheduler_job_run_details where job_name=:job_name and to_date(trunc(actual_start_date))=trunc(sysdate)-1''',job_name=job_name)
        for val in self.cursor:
            if int(val[0])==0:
                return False
            elif int(val[0])==1:
                return True
            else:
                return None

    def return_job_status(self,job_name):
        self.cursor.execute('''select status,actual_start_date,run_duration from user_scheduler_job_run_details where job_name=:job_name and to_date(trunc(actual_start_date))=trunc(sysdate)-1''',job_name=job_name)
        for status,actual_start_date,run_duration_time in self.cursor:
            return (f'A status for {job_name} job in unit {self.instance} is {status},actual_start_date:{actual_start_date},run_duration_time:{run_duration_time}')



    def check_runinng_jobs(self,job_name):

        self.cursor.execute("select count(1) from user_scheduler_running_jobs where job_name=:jobname",jobname=job_name)
        for val in self.cursor:
            if int(val[0])==0:
                return False
            elif int(val[0])==1:
                return True
            else:
                return None

    def get_set_flag(self,flag_val,job_name):

        if flag_val==0:
            with open(check_job_status.flag_file,'r') as flag:
                try:
                    reader = csv.reader(flag,delimiter=',',)
                    for line in reader:
                        if line[1] == self.instance and line[2] == job_name:
                            return line[0],line[2]
                        else:
                            continue
                    return None
                except IndexError:
                    return None
        #if we haven't found an instance entry with a flag 0, we provide flag 2 to append a line with instance
        elif flag_val==2:
            with open(check_job_status.flag_file, 'a') as flag:
                writer = csv.writer(flag)
                writer.writerow([check_job_status.today,self.instance,job_name])

        else:
            file = pd.read_csv(check_job_status.flag_file,header=0)
            # file.loc[file['Instance']==self.instance,"Date"] = check_job_status.today
            file.loc[(file['Instance'] == self.instance) & (file['JobName'] == job_name), "Date"] = check_job_status.today
            file.to_csv(check_job_status.flag_file,index=False)


    def send_mail(self,text,job_name,instance):
        HOST = "localhost"
        SUBJECT = f'STATUS OF THE JOB {job_name} IN UNIT {instance}'
        TO = ["aleksei.semerikov@ringcentral.com"]
        FROM = "aleksei.semerikov@ringcentral.com"
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
        #check for unit readonly
        if not self.check_readonly_status():
            logger.warning(f'A unit {self.instance} in read/write mode')
            for job_name in self.job_list:
            # check if the job is still running
                if not self.check_job_completed(job_name) and self.check_runinng_jobs(job_name):
                    # self.send_mail('Job is still running')
                    logger.warning(f'Job is still running')
            #if a job is completed
                elif self.check_job_completed(job_name) and not self.check_runinng_jobs(job_name):

            #if get_set_flag(0) returns None = record not found we append a list or records in send_today_flag file
                    if self.get_set_flag(0,job_name) is None:
                        self.get_set_flag(2,job_name)
                        # self.send_mail(self.return_job_status())
                        print(self.return_job_status(job_name))

            #we check if we have a record for today and we do =>skip
                    elif self.get_set_flag(0,job_name)[0]==check_job_status.today and self.get_set_flag(0,job_name)[1] == job_name:
                        pass



            #otherwise change information in send_today_flag file for a given instance
                    else:
                        self.get_set_flag(1,job_name)
                        # self.send_mail(self.return_job_status())
                        print(self.return_job_status(job_name))

            # the job hasn't been started yet
                else:
                    return (f'Job hasn"t been started today yet')

        else:
            return (f'A unit {self.instance} is in read mode. Jobs is not running here')

list = ['PRO-ADB311','PRO-ADB312','PRO-ADB321','PRO-ADB322','PRO-ADB331','PRO-ADB332','PRO-ADB341',
        'PRO-ADB342','PRO-ADB351','PRO-ADB352','PRO-ADB361','PRO-ADB362']
# list=['PRO-ADB351','PRO-ADB352']
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