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
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.markdown import bold
import aiogram.utils.markdown as fmt

logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7619938635:AAGumItYqcYnXOmHFK5zoDlLkTroU4MRkV8")
# Диспетчер
dp = Dispatcher()

#print("MEXC Futures price: ", mexc.get_futures_mexc_price("JUP_USDT"))
#print("MEXC Spot price: ", mexc.get_spot_mexc_price("JUPUSDT"))
#print("Dex Screener price: ", ds.GetDexScreenerPrice("solana", "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"))
#print("GMGN AI price: ", gmgn.GetGmgnPrice("https://gmgn.ai/sol/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"))

# types.InlineKeyboardButton(text="GMGN", url="https://gmgn.ai/sol/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"),
#        types.InlineKeyboardButton(text="MEXC", url="https://futures.mexc.com/ru-RU/exchange/JUP_USDT?utm_source=mexc&utm_medium=pagehowtobuyfuturesbuttonJUP&utm_campaign=pagefuturesJUP&inviteCode=mexc-HtbFuBuFutu")
#    ]
#
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    mexc_fut = mexc.get_futures_mexc_price("JUP_USDT")
    mexc_spot = mexc.get_spot_mexc_price("JUPUSDT")
    dex_price = ds.GetDexScreenerPrice("solana", "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN")
    spred1 = round(100 - ((float(mexc_fut)/float(dex_price))*100), 5)
    spred2 = round(100 - ((float(mexc_spot)/float(dex_price))*100), 5)

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="GMGN", url="https://gmgn.ai/sol/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN")],
        [types.InlineKeyboardButton(text="MEXC", url="https://futures.mexc.com/ru-RU/exchange/JUP_USDT?utm_source=mexc&utm_medium=pagehowtobuyfuturesbuttonJUP&utm_campaign=pagefuturesJUP&inviteCode=mexc-HtbFuBuFutu")]
    ])

    await message.answer(
        fmt.text(
            fmt.text(fmt.hbold("Token:  JUP")),
            fmt.text(fmt.hbold("MEXC Spot"), (mexc_spot)),
            fmt.text(fmt.hbold("MEXC-DEX"),  spred1),
            fmt.text(fmt.hbold("SPOT-DEX"), spred2),
            fmt.text(fmt.hbold("MEXC Futures"), mexc_fut),
            fmt.text(fmt.hbold("DEX Screener"), dex_price),
            sep="\n\n",

        ),
        parse_mode="HTML",
        reply_markup=keyboard  # Добавляем клавиатуру к сообщению
    )

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
