import requests
from pprint import pprint
api_key = 'u+7LeyzwG9TFtUzYWStg'
header={'Authorization': 'Token token=u+7LeyzwG9TFtUzYWStg'}
#query={'query':'DBA-OPS@Critical Alerts'}
query={'escalation_policy_ids[]':['PBAKSVU']}
#with requests.get('https://api.pagerduty.com/escalation_policies',headers=header,params=query) as link:
with requests.get('https://api.pagerduty.com/oncalls', headers=header, params=query) as link:
    data=link.json()
    pprint(data)
    # for on_calls in data.get('oncalls')[:1]:
    #     pprint(on_calls)

