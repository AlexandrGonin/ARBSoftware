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
KET = ["KET_USDT", "KETUSDT", "KETyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"]
DHN = ["DHN_USDT", "DHNUSDT", "DHNyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"]
YZYSQL = ["YZYSQL_USDT", "YZYSQLUSDT", "YZYSQLyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"]
EGG = ["EGG_USDT", "EGGUSDT", "EGGyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"]
A8 = ["A8_USDT", "A8USDT", "A8yiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"
        ]
while True:
    dex = ds.GetDexScreenerPrice("solana", "zu5nvbnvwfzau7dv8tozjumjyerbw4na4ujnhytuxqp")
    #dex_price = [ds.GetDexScreenerPrice("solana", KET[2]), ds.GetDexScreenerPrice("solana", DHN[2]), ds.GetDexScreenerPrice("solana", YZYSQL[2]), ds.GetDexScreenerPrice("solana", EGG[2]), ds.GetDexScreenerPrice("solana", A8[2])]
    print(dex)


