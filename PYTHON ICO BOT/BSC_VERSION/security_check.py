import requests
from pprint import pprint


# def is_scam(token):
#     with requests.get(f'https://api.gopluslabs.io/api/v1/token_security/56?contract_addresses={token}') as link:
#         if link.status_code == 200:
#             data = link.json()
#             data = data['result'][token.lower()]
#             # pprint(data)
#             if data['is_open_source'] and data['honeypot_with_same_creator'] == 0:
#                 if any(data['anti_whale_modifiable'],data['can_take_back_ownership'],data['is_proxy'],data['is_honeypot'],data['is_mintable'],data['is_blacklisted'],
#                        data['is_anti_whale'],data['is_whitelisted'],data['trading_cooldown'],data['selfdestruct'],data['hidden_owner'],data['can_take_back_ownership']):
#                     return True
#                 else:
#                     return False
#             else:
#                 return True
#
#
#
#
#
#
# print(is_scam('0x543554207B4c79c58fe6A3c3c45745E0F1a8963F'))



if any([True,False,False,False,False,False,False]):
    print('True')