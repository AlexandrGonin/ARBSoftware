import requests
import json
import asyncio
import aiohttp

chain_id = "solana"  # Correct chain ID
token_address = "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"  # Your token address

async def get_request_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def GetDexScreenerPrice(chain_id, token_address):
    """
    Retrieves data about token pairs from Dexscreener API for a given chain and token address.

    Args:
        chain_id (str): The chain ID (e.g., "solana").
        token_address (str): The token address.

    Returns:
        dict or None: A dictionary containing the response data, or None if an error occurs.
    """
    url = f"https://api.dexscreener.com/token-pairs/v1/{chain_id}/{token_address}"

    try:
        response_text = await get_request_async(url)
        return response_text[0]["priceUsd"]

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
# Example Usage:


#print(GetDexScreenerPrice("solana", "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"))