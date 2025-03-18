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

logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7619938635:AAGumItYqcYnXOmHFK5zoDlLkTroU4MRkV8")
# Диспетчер
dp = Dispatcher()

types.InlineKeyboardButton(text="GMGN", url="https://gmgn.ai/sol/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"), types.InlineKeyboardButton(text="MEXC", url="https://futures.mexc.com/ru-RU/exchange/JUP_USDT?utm_source=mexc&utm_medium=pagehowtobuyfuturesbuttonJUP&utm_campaign=pagefuturesJUP&inviteCode=mexc-HtbFuBuFutu")


# Списки ниже содержат по 3 элемента - ключевые слова для разных обменников [mex_fut, mex_spot, dex_price]

KET = ["KET_USDT", "KETUSDT", "KETyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"]
DHN = ["DHN_USDT", "DHNUSDT", "DHNyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"]
YZYSQL = ["YZYSQL_USDT", "YZYSQLUSDT", "YZYSQLyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"]
EGG = ["EGG_USDT", "EGGUSDT", "EGGyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"]
A8 = ["A8_USDT", "A8USDT", "A8yiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"]


while True:
    # mexc_fut = [mexc.get_futures_mexc_price(KET[0]), mexc.get_futures_mexc_price(DHN[0]), mexc.get_futures_mexc_price(YZYSQL[0]), mexc.get_futures_mexc_price(EGG[0]), mexc.get_futures_mexc_price(A8[0])]
    # mexc_spot = [mexc.get_spot_mexc_price(KET[1]),mexc.get_spot_mexc_price(KET[1]), mexc.get_spot_mexc_price(DHN[1]),mexc.get_spot_mexc_price(YZYSQL[1]),mexc.get_spot_mexc_price(EGG[1]),mexc.get_spot_mexc_price(A8[1])]
    # dex_price = [ds.GetDexScreenerPrice("solana", KET[2]), ds.GetDexScreenerPrice("solana", DHN[2]), ds.GetDexScreenerPrice("solana", YZYSQL[2]), ds.GetDexScreenerPrice("solana", EGG[2]), ds.GetDexScreenerPrice("solana", A8[2])]
    # spred1 = round(100 - ((float(mexc_fut)/float(dex_price))*100), 5)
    # spred2 = round(100 - ((float(mexc_spot)/float(dex_price))*100), 5)
    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        await message.answer(
            "12345"
        )
    
    async def main():
        await dp.start_polling(bot)
    
    time.sleep(2)
    



#print("MEXC Futures price: ", mexc.get_futures_mexc_price("JUP_USDT"))
#print("MEXC Spot price: ", mexc.get_spot_mexc_price("JUPUSDT"))
#print("Dex Screener price: ", ds.GetDexScreenerPrice("solana", "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"))
#print("GMGN AI price: ", gmgn.GetGmgnPrice("https://gmgn.ai/sol/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"))




# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     mexc_fut = mexc.get_futures_mexc_price("JUP_USDT")
#     mexc_spot = mexc.get_spot_mexc_price("JUPUSDT")
#     dex_price = ds.GetDexScreenerPrice("solana", "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN")
#     spred1 = round(100 - ((float(mexc_fut)/float(dex_price))*100), 5)
#     spred2 = round(100 - ((float(mexc_spot)/float(dex_price))*100), 5)

#     keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
#         [types.InlineKeyboardButton(text="GMGN", url="https://gmgn.ai/sol/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN")],
#         [types.InlineKeyboardButton(text="MEXC", url="https://futures.mexc.com/ru-RU/exchange/JUP_USDT?utm_source=mexc&utm_medium=pagehowtobuyfuturesbuttonJUP&utm_campaign=pagefuturesJUP&inviteCode=mexc-HtbFuBuFutu")]
#     ])

#     await message.answer(
#         fmt.text(
#             fmt.text(fmt.hbold("Token:  JUP")),
#             fmt.text(fmt.hbold("MEXC Spot"), (mexc_spot)),
#             fmt.text(fmt.hbold("MEXC-DEX"),  spred1),
#             fmt.text(fmt.hbold("SPOT-DEX"), spred2),
#             fmt.text(fmt.hbold("MEXC Futures"), mexc_fut),
#             fmt.text(fmt.hbold("DEX Screener"), dex_price),
#             sep="\n\n",

#         ),
#         parse_mode="HTML",
#         reply_markup=keyboard  # Добавляем клавиатуру к сообщению
#     )

# # Запуск процесса поллинга новых апдейтов
# async def main():
#     await dp.start_polling(bot)

