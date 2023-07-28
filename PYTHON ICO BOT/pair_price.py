def get_min_amount_to_buy(self, token_in, token_out, amount_to_buy):
    try:
    decimals_in = ICO_BOT.w3.eth.contract(address=token_in, abi=ERC20_ABI).functions.decimals().call()#сделаю через смарт контракт
    smallest_unit_amount_to_buy = amount_to_buy * (10 ** (18 - decimals_in))
    res = ICO_BOT.my_contract.functions.getAmountOutMin(token_in, token_out, smallest_unit_amount_to_buy).call()
    decimals_out = ICO_BOT.w3.eth.contract(address=token_out, abi=ERC20_ABI).functions.decimals().call()
    normal_unit_res = res / (10 ** (18 - decimals_out))
    print(f'It should return about {normal_unit_res} of token {token_out} for {amount_to_buy} of {token_in} token')
    return normal_unit_res
    except web3.exceptions.ContractLogicError:
        print(f'Not enough liquidity. Try another pair or another amount')
        return None

def swap_token(self, token_in, token_out, amount_to_buy):
    amount_out_min = self.get_min_amount_to_buy(token_in, token_out, amount_to_buy)
    if amount_out_min is not None and amount_out_min != 0:
        nonce = ICO_BOT.w3.eth.get_transaction_count(ICO_BOT.my_address_in_goeri)
        tx = ICO_BOT.my_contract.functions._swap_token(token_in, token_out, amount_to_buy, amount_out_min, ICO_BOT.my_contract_address).build_transaction({'nonce':nonce,'gas':ICO_BOT.g as})
        signed_tx = ICO_BOT.w3.eth.account.signTransaction(tx, ICO_BOT.private_key)
        ICO_BOT.w3.eth.sendRawTransaction(signed_tx.rawTransaction)





# def get_min_amount_to_buy(self, token_in, token_out, amount_to_buy):
#     try:
#     Get the number of decimals of token_in decimals_in = ICO_BOT.w3.eth.contract(address=token_in, abi=ERC20_ABI).functions.decimals().call()
#     Convert amount_to_buy to the smallest unit of token_in smallest_unit_amount_to_buy = amount_to_buy * (10 ** (18 - decimals_in))
#   Get the minimum amount of token_out required to buy amount_to_buy of token_in res = ICO_BOT.my_contract.functions.getAmountOutMin(token_in, token_out, smallest_unit_amount_to_buy).call()
#   Convert the minimum amount of token_out to the normal unit (not the smallest unit) decimals_out = ICO_BOT.w3.eth.contract(address=token_out, abi=ERC20_ABI).functions.decimals().call()
#   normal_unit_res = res / (10 ** (18 - decimals_out))
#   print(f'It should return about {normal_unit_res} of token {token_out} for {amount_to_buy} of {token_in} token')
#   return normal_unit_res
#   except web3.exceptions.ContractLogicError:
#   print(f'Not enough liquidity. Try another pair or another amount')
#   return None
#   def swap_token(self, token_in, token_out, amount_to_buy):
# Get the minimum amount of token_out required to buy amount_to_buy of token_in amount_out_min = self.get_min_amount_to_buy(token_in, token_out, amount_to_buy)
# if amount_out_min is not None and amount_out_min != 0:
# nonce = ICO_BOT.w3.eth.get_transaction_count(ICO_BOT.my_address_in_goeri)
# tx = ICO_BOT.my_contract.functions._swap_token(token_in, token_out, amount_to_buy, amount_out_min, ICO_BOT.my_contract_address).build_transaction({'nonce':nonce,'gas':ICO_BOT.gas})
# signed_tx = ICO_BOT.w3.eth.account.signTransaction(tx, ICO_BOT.private_key) ICO_BOT.w3.eth.sendRawTransaction(signed_tx.rawTransaction)




def swap_token(self, token_in, token_out, amount_to_buy):
# Get the decimal precision of the tokens
token_in_decimals = self.get_decimals(token_in)
token_out_decimals = self.get_decimals(token_out)

# Calculate the scaling factor based on the decimal precision of the tokens
scaling_factor = 10 ** (token_in_decimals - token_out_decimals)

# Adjust the amount of token_in based on the scaling factor
adjusted_amount_to_buy = amount_to_buy / scaling_factor

# Get the minimum amount of token_out that can be bought for the adjusted amount of token_in
min_amount_out = self.get_min_amount_to_buy(token_in, token_out, adjusted_amount_to_buy)

# Check if there is enough liquidity to perform the swap
if min_amount_out is not None and min_amount_out != 0:
# Get the current nonce for the account
nonce = ICO_BOT.w3.eth.get_transaction_count(ICO_BOT.my_address_in_goeri)

# Build the transaction to perform the swap
tx = ICO_BOT.my_contract.functions._swap_token(
token_in, token_out, adjusted_amount_to_buy, min_amount_out, ICO_BOT.my_contract_address
).build_transaction({"nonce": nonce, "gas": ICO_BOT.gas})

# Sign the transaction
signed_tx = ICO_BOT.w3.eth.account.sign_transaction(tx, ICO_BOT.private_key)

# Send the signed transaction
ICO_BOT.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
else:
print(f"we cannot swap these tokens due to the lack of liquidity")
return None

def get_min_amount_to_buy(self, token_in, token_out, amount_to_buy):
try:
# Call the getAmountOutMin function on the contract to get the minimum amount of token_out that can be bought
res = ICO_BOT.my_contract.functions.getAmountOutMin(token_in, token_out, amount_to_buy).call()
print(f"It should return about {res} of token {token_out} for {amount_to_buy} of {token_in} token")
return res
except web3.exceptions.ContractLogicError:
print(f"Not enough liquidity. Try another pair or another amount")
return None
