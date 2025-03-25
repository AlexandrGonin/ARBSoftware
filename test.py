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
while True:
    mexc_fut = mexc.get_futures_mexc_price(A8[0])
    dex_price = ds.GetDexScreenerPrice("ethereum", A8[2])
    
    print(mexc_fut, dex_price)


