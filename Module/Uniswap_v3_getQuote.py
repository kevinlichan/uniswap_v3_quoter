import json
from web3 import Web3
from Module.Constants.Uniswap_v3_Quoter import abi

# Load environment
data = open('./Module/Constants/environment.json')
env = json.loads(data.read())

# Load token data
data = open('./Module/Constants/tokens.json')
tokens = json.loads(data.read())

# Connect to web3 provider
url = env['URL']
web3 = Web3(Web3.HTTPProvider(url))

# Uniswap v3 Quoter Contract
contract_address = env['CONTRACT']
contract = web3.eth.contract(address=contract_address, abi=abi)

def quote(_tokenIn, _tokenOut, _amountIn):

    ## Web3 connection
    if not web3.isConnected():
        print("Not connected to any network")
        return

    ## Fee Tiers
    feeTiers = [100, 500, 3000, 10000]
    quotes = {}
    
    ## Converting to raw amount
    _amountInRaw = int(_amountIn * 10 ** int(tokens[_tokenIn]['decimals']))

    ## Call the Uniswap v3 Quoter Contract
    for _feeTier in feeTiers:
        try:
            _amountOutRaw = contract.functions.quoteExactInputSingle(tokens[_tokenIn]['address'], tokens[_tokenOut]['address'], _feeTier, _amountInRaw, 0).call()
            _amountOut = _amountOutRaw / (10 ** int(tokens[_tokenOut]['decimals']))
            feeTier = str(_feeTier / 10000) + '%'
            quotes[feeTier] = _amountOut
        except:
            pass

    return quotes