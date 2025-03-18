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
DHN = ["DHN_USDT", "DHNUSDT", "0x1dcd41a3876959023ef49603374af655973a64cf"]
YZYSQL = ["YZYSQL_USDT", "YZYSQLUSDT", "YZYSQLyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"]
EGG = ["EGG_USDT", "EGGUSDT", "EGGyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"]
A8 = ["A8_USDT", "A8USDT", "A8yiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"]
while True:
    dex_price = [ds.GetDexScreenerPrice("avalanche", KET[2]), ds.GetDexScreenerPrice("ethereum", DHN[2]), ds.GetDexScreenerPrice("solana", YZYSQL[2]), ds.GetDexScreenerPrice("solana", EGG[2]), ds.GetDexScreenerPrice("solana", A8[2])]
    mexc_fut = [mexc.get_futures_mexc_price(KET[0]), mexc.get_futures_mexc_price(DHN[0]), mexc.get_futures_mexc_price(YZYSQL[0]), mexc.get_futures_mexc_price(EGG[0]), mexc.get_futures_mexc_price(A8[0])]
    print(mexc_fut, dex_price)


