import requests

import asyncio
import aiohttp
import json

async def get_request_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def get_futures_mexc_price(symbol):
    try:
        url = f"https://contract.mexc.com/api/v1/contract/fair_price/{symbol}"

        response_text = await get_request_async(url)
        return response_text['data']['fairPrice']


    except requests.exceptions.RequestException as e:
        #print(f"Ошибка при запросе к API MEXC: {e}")
        return None

    except (KeyError, json.JSONDecodeError) as e:
        #print(f"Ошибка при обработке ответа API: {e}")
        return None


print(get_futures_mexc_price(["BTC_USDT"]))