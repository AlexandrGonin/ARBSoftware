import requests
import json

chain_id = "solana"  # Correct chain ID
token_address = "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"  # Your token address

def GetDexScreenerPrice(chain_id, token_address):
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
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        #return data

        strDEXPrice =json.dumps(data[0]["priceUsd"], indent=2)
        strDEXPrice = strDEXPrice.strip('"')
        DEXPrice = float(strDEXPrice)
        return DEXPrice

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        print(f"Response text: {response.text}")  # Print raw response for debugging
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
# Example Usage:


#print(GetDexScreenerPrice("solana", "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"))