import asyncio
import json
import requests

import aiohttp

chain_id = "solana"  # Correct chain ID
token_address = "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"  # Your token address

url = f"https://api.dexscreener.com/token-pairs/v1/{chain_id}/{token_address}"

response = requests.get(url)
response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
data = response.json()
#return data

strDEXPrice =json.dumps(data[0]["priceUsd"], indent=2)
strDEXPrice = strDEXPrice.strip('"')
DEXPrice = float(strDEXPrice)
print(DEXPrice)

async def get_request_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def main():
    url = f"https://api.dexscreener.com/token-pairs/v1/{chain_id}/{token_address}"
    response_text = await get_request_async(url)
    print(response_text[0]["priceUsd"])

asyncio.run(main())