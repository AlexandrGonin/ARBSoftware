import sys
sys.path.append("dex screener")
sys.path.append("gmgn")
sys.path.append("mexc")
import dex_screener_api as ds
import gmgn_api as gmgn
import mexc_api as mexc


import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7619938635:AAGumItYqcYnXOmHFK5zoDlLkTroU4MRkV8")
# Диспетчер
dp = Dispatcher()

#print("MEXC Futures price: ", mexc.get_futures_mexc_price("JUP_USDT"))
#print("MEXC Spot price: ", mexc.get_spot_mexc_price("JUPUSDT"))
#print("Dex Screener price: ", ds.GetDexScreenerPrice("solana", "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"))
#print("GMGN AI price: ", gmgn.GetGmgnPrice("https://gmgn.ai/sol/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"))


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    mexc_fut = mexc.get_futures_mexc_price("JUP_USDT") 
    mexc_spot = mexc.get_spot_mexc_price("JUPUSDT")
    dex_price = ds.GetDexScreenerPrice("solana", "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN")
    spred1 = round(100 - ((float(mexc_fut)/float(dex_price))*100), 5)
    await message.answer("Price:")
    await message.answer("Mexc futures: "+str(mexc_fut))
    await message.answer("Mexc spot: "+str(mexc_spot))
    await message.answer("Dex price: "+str(dex_price))
    if spred1>0:
        await message.answer("Спред (fut-dex): "+str(spred1))
    elif spred1==0:
        await message.answer("Спред = 0")
    else:
        await message.answer("Спред < 0")
#    await message.answer(str(gmgn.GetGmgnPrice()))


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())