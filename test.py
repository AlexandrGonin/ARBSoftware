import sys
sys.path.append("dex screener")
sys.path.append("gmgn")
sys.path.append("mexc")
import dex_screener_api as ds
#import gmgn_api as gmgn
import mexc_api as mexc

import asyncio
import logging
import aiogram
import time
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.markdown import bold
import aiogram.utils.markdown as fmt
KET = ["KET_USDT", "KETUSDT", "0xFFFF003a6BAD9b743d658048742935fFFE2b6ED7"]
DHN = ["DHN_USDT", "DHNUSDT", "0x32462bA310E447eF34FF0D15BCE8613aa8C4A244"]
A8 = ["A8_USDT", "A8USDT", "0x3E5A19c91266aD8cE2477B91585d1856B84062dF"]

async def main(): 
    TEST = ["TIBBIR","TIBBIR_USDT","0xA4A2E2ca3fBfE21aed83471D28b6f65A233C6e00","base"]
    while True:
        c=0
        mexc_fut,dex_price,spreds,tasks=[],[],[],[]
        
        mexc_fut_value = asyncio.create_task(mexc.get_futures_mexc_price(TEST[1]))
        dex_price_value = asyncio.create_task(ds.GetDexScreenerPrice(TEST[3], TEST[2]))
    
        tasks.append(mexc_fut_value)
        tasks.append(dex_price_value)

        results = await asyncio.gather(*tasks)
        for result in results:
            print("mexc: ",result, end="  ") if c%2==0 else print("dex: ",result)	
            c+=1


if __name__ == "__main__":
    asyncio.run(main())
