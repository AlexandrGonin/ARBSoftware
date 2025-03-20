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

delay = 0
chat_id=1353395168


types.InlineKeyboardButton(text="GMGN", url="https://gmgn.ai/sol/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"), types.InlineKeyboardButton(text="MEXC", url="https://futures.mexc.com/ru-RU/exchange/JUP_USDT?utm_source=mexc&utm_medium=pagehowtobuyfuturesbuttonJUP&utm_campaign=pagefuturesJUP&inviteCode=mexc-HtbFuBuFutu")


# Списки ниже содержат по 3 элемента - ключевые слова для разных обменников [mex_fut, mex_spot, dex_price]

KET = ["KET_USDT", "0xFFFF003a6BAD9b743d658048742935fFFE2b6ED7"]
DHN = ["DHN_USDT", "DHNyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"]
YZYSQL = ["YZYSQL_USDT", "YZYSQLyiwrYJFskUPiHa7hkeR8V UtAeFoSYbKedZNsDvCN"]
EGG = ["EGG_USDT", "EGGyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"]
A8 = ["A8_USDT", "A8yiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"]

async def condition_check_loop(chat_id):
    max_spred=0
    cond = False
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="MEXC", url="https://futures.mexc.com/ru-RU/exchange/KET_USDT")]
    ])
    while True:
        mexc_fut = [mexc.get_futures_mexc_price(KET[0])]
        dex_price = [ds.GetDexScreenerPrice("avalanche", KET[1])]
        spred = round(100 - ((float(mexc_fut[0])/float(dex_price[0]))*100), 5)
        # spred2 = round(100 - ((float(mexc_spot)/float(dex_price))*100), 5)
        if abs(spred)>max_spred:
            max_spred=abs(spred)

        print(mexc_fut, dex_price, spred, max_spred)
        time.sleep(delay)

        if abs(spred) > 4 and cond == False:
            await bot.send_message(chat_id,
                fmt.text(
                    fmt.text(fmt.hbold("Token:  KET")),
                    fmt.text(fmt.hbold("MEXC Futures"), mexc_fut),
                    fmt.text(fmt.hbold("DEX Screener"), dex_price),
                    fmt.text(fmt.hbold("Спред: "),  spred),
                    fmt.text(fmt.hbold("Открыть short")),
                    
                    sep="\n\n",),parse_mode="HTML",reply_markup=keyboard)  # Добавляем клавиатуру к сообщению
            cond = True
        elif abs(spred) < 1 and cond == True:
            cond = False
            await bot.send_message(chat_id,
                fmt.text(
                    fmt.text(fmt.hbold("Token:  KET")),
                    fmt.text(fmt.hbold("MEXC Futures"), mexc_fut),
                    fmt.text(fmt.hbold("DEX Screener"), dex_price),
                    fmt.text(fmt.hbold("Спред: "),  spred),
                    fmt.text(fmt.hbold("Закрыть short")),
                    sep="\n\n",), parse_mode="HTML",reply_markup=keyboard)

        #await bot.send_message(chat_id, "Цена mex_fut: "+str(*mexc_fut)+" Цена dex: "+str(dex_price)+" Спред: "+str(spred)+" Макс. спред: "+str(max_spred))
    
@dp.message(Command("start"))
async def subscribe_to_condition(message: types.Message):
    chat_id = message.chat.id
    # Правильный вызов асинхронной функции с использованием await
    await condition_check_loop(chat_id)

async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())

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

