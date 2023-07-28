from decimal import *
# reserve1 = 673593746796161410947171271
# reserve0 = 11903217257046646920
# decimal0 = 18
# decimal1 = 18
# Res0Normalized  = reserve0*(10 ** (decimal1-decimal0))
# price = reserve1*(10 ** 18)/Res0Normalized
# print(price)

#
# price = (reserve0 * 10**decimal0) / (reserve1 * 10**decimal1)
# print(price)
from uniswap import Uniswap

address = '0x96670E97EB5fe41Fbfe0Df83F1eA24aA14c26E86'
private_key='ce3038308761279b92fcffb1b8ae7dbd5ce113463a663257438e3945353e21d1'
version=2
provider = 'https://mainnet.infura.io/v3/6cda95a972fe4e168a9057235825b257'
uniswap = Uniswap(address=address, private_key=private_key, version=version, provider=provider)


print(uniswap.get_raw_price('0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2', '0x3f40fb0f3c9d1dbb264effa29dd9fc302f97e9be', 10**18))
# print(uniswap.get_price_input())