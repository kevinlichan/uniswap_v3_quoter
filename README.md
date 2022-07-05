# Uniswap v3 Quoter

Simple python module to read the Uniswap v3 Quoter smart contract to aggregate quotes across all pools and fee tiers available on Uniwap v3. 

## Environment Details

Uniswap v3 Quoter Contract: `0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6`

## Running Uniswap v3 Quoter

Navigate to the project directory:
`cd Project Folder`

Edit run.py to specify your input and output token (e.g. WBTC, USDC):

`quote(INPUT_TOKEN_TICKER, OUTPUT_TOKEN_TICKER, INPUT_TOKEN_AMOUNT)`

Run the script:
`python run.py`

Example Output:

`{'0.3%': 19280.039817, '1.0%': 19112.449151}`

## Dependencies

- Web3 HTTP Provider URL
- token.json (list of ERC-20 tokens)
