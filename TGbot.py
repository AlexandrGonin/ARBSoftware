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
bot = Bot(token="8031545073:AAFppT7ziBlV3vpkn9zflITk_GmPnLSYpDY")
dp = Dispatcher()

delay = 0
chat_id=(-1002501950419)

KET = ["KET", "KET_USDT", "0xFFFF003a6BAD9b743d658048742935fFFE2b6ED7", "avalanche"]
DHN = ["DHN", "DHN_USDT", "0x32462bA310E447eF34FF0D15BCE8613aa8C4A244", "ethereum"]
A8 = ["A8", "A8_USDT", "0x3E5A19c91266aD8cE2477B91585d1856B84062dF", "ethereum"]
JUP = ["JUP", "JUP_USDT", "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN", "solana"]
tokens=[DHN,A8,JUP]
tasks = []

async def bot_loop(chat_id):
    c=0
    conds = [False]*len(tokens)
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="MEXC", url="https://futures.mexc.com/ru-RU/exchange/KET_USDT")]
    ])
    mexc_fut,dex_price,spreds=[],[],[]
    while True:
        c=0
        mexc_fut,dex_price,spreds,tasks=[],[],[],[]
        for num in range(len(tokens)):
            mexc_fut_value = asyncio.create_task(mexc.get_futures_mexc_price(tokens[num][1]))
            dex_price_value = asyncio.create_task(ds.GetDexScreenerPrice(tokens[num][3], tokens[num][2]))
  
            tasks.append(mexc_fut_value)
            tasks.append(dex_price_value)

        results = await asyncio.gather(*tasks)
        for result in results:
            mexc_fut.append(result) if c%2==0 else dex_price.append(result)	
            c+=1
        
        await asyncio.sleep(delay)

        for num in range(len(tokens)):
            spreds.append(round(100 - ((float(mexc_fut[num])/float(dex_price[num]))*100), 5))
            print("{",mexc_fut[num], dex_price[num], spreds[num],"}  ",end="")

        print("   ")
        
        for num in range(len(tokens)):
            if spreds[num] < -5 and conds[num] == False:
                bot.send_message(chat_id,
                    fmt.text(
                        fmt.text(fmt.hbold("Token: ", tokens[num][0])),
                        fmt.text(fmt.hbold("MEXC Futures"), mexc_fut[num]),
                        fmt.text(fmt.hbold("DEX Screener"), dex_price[num]),
                        fmt.text(fmt.hbold("Спред: "),  spreds[num]),
                        fmt.text(fmt.hbold("Открыть short")),

                        sep="\n\n",),parse_mode="HTML",reply_markup=keyboard)  # Добавляем клавиатуру к сообщению
                conds[num] = True
            elif spreds[num] > -1 and conds[num] == True:
                conds[num] = False
                await bot.send_message(chat_id,
                    fmt.text(
                        fmt.text(fmt.hbold("Token: ", tokens[num][0])),
                        fmt.text(fmt.hbold("MEXC Futures"), mexc_fut[num]),
                        fmt.text(fmt.hbold("DEX Screener"), dex_price[num]),
                        fmt.text(fmt.hbold("Спред: "),  spreds[num]),
                        fmt.text(fmt.hbold("Закрыть short")),
                        sep="\n\n",), parse_mode="HTML",reply_markup=keyboard)

    
@dp.message(Command("start"))
async def starting(message: types.Message):
    chat_id = message.chat.id
    await bot_loop(chat_id)

async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
