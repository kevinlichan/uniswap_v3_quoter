from Module.Uniswap_v3_getQuote import quote

# Call the quote function connected to Uniswap v3
## inputs: quote(Token, Quote_Token, Quantity)
## outputs: {feetier: quote}
result = quote("WBTC", "USDC", 1)
print(result)