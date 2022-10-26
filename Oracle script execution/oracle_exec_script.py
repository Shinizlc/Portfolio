##first option using subprocess
import subprocess as sp
from loguru import logger
import os
from columnar import Columnar
os.environ['PATH']='/Users/aleksei.semerikov/OracleClient/instantclient_12_2:/Users/aleksei.semerikov/OracleClient/instantclient_12_2:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/Library/Frameworks/Mono.framework/Versions/Current/Commands'
os.environ['TNS_ADMIN']='/Users/aleksei.semerikov/OracleClient/instantclient_12_2/network'
os.environ['ORACLE_HOME']='/Users/aleksei.semerikov/OracleClient/instantclient_12_2'

# list_of_db=['PRO-ADB011', 'PRO-ADB012','PRO-ADB021', 'PRO-ADB022','PRO-ADB031', 'PRO-ADB032','PRO-ADB041', 'PRO-ADB042','PRO-ADB051','PRO-ADB052',
# 'PRO-ADB061', 'PRO-ADB062','PRO-ADB071', 'PRO-ADB072','PRO-ADB081','PRO-ADB082','PRO-ADB101','PRO-ADB102','PRO-ADB111',
# 'PRO-ADB112','PRO-ADB121','PRO-ADB122','PRO-ADB131','PRO-ADB132','PRO-ADB141','PRO-ADB142','PRO-ADB151','PRO-ADB152','PRO-ADB161','PRO-ADB162',
# 'PRO-ADB171','PRO-ADB172','PRO-ADB201','PRO-ADB202','PRO-ADB211','PRO-ADB241','PRO-ADB242','PRO-ADB311','PRO-ADB312','PRO-ADB321',
# 'PRO-ADB322','PRO-ADB331','PRO-ADB332','PRO-ADB341','PRO-ADB342','PRO-ADB351','PRO-ADB352','PRO-ADB361','PRO-ADB362']
#
list_of_db=['PRO-ADB311','PRO-ADB312','PRO-ADB321','PRO-ADB322','PRO-ADB331',
            'PRO-ADB332','PRO-ADB341','PRO-ADB342','PRO-ADB351','PRO-ADB352','PRO-ADB361','PRO-ADB362']






# list_of_db=['OPS-STG-ADB011','OPS-STG-ADB012','OPS-STG-ADB021','OPS-STG-ADB022']

with open('31-36pods.log', 'w') as file:
    for db in list_of_db:
    #why do we need the stdin=sp.PIPE even if we don't use input(I can't see the output without it)
        with sp.Popen(['sqlplus','system/euLagoon2209@'+db,'@sql_script.sql'],stdin=sp.PIPE,stdout=sp.PIPE,stderr=sp.PIPE) as com:
            out,err = com.communicate()
            file.writelines('\n')
            file.writelines('\n')
            file.writelines('\n')
            file.writelines(f'###################################'+'\n')
            file.writelines(f'DATA From database {db}:')
            for line in out.decode().splitlines():
                file.writelines(line+'\n')





