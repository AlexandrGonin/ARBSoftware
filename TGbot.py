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

delay = 1.5
chat_id=(-1002501950419)

KET = ["KET", "KET_USDT", "0xFFFF003a6BAD9b743d658048742935fFFE2b6ED7", "avalanche"]

DHN = ["DHN", "DHN_USDT", "0x32462bA310E447eF34FF0D15BCE8613aa8C4A244", "ethereum"]
A8 = ["A8", "A8_USDT", "0x3E5A19c91266aD8cE2477B91585d1856B84062dF", "ethereum"]
JUP = ["JUP", "JUP_USDT", "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN", "solana"]
DOGINME = ["DOGINME","DOGINME_USDT","0x6921B130D297cc43754afba22e5EAc0FBf8Db75b","base"]
MUBARAK = ["MUBARAK","MUBARAK_USDT","0x5C85D6C6825aB4032337F11Ee92a72DF936b46F6","bsc"]
TUT = ["TUT","TUT_USDT","0xCAAE2A2F939F51d97CdFa9A86e79e3F085b799f3","bsc"]
FORM = ["FORM","FORM_USDT","0x5b73A93b4E5e4f1FD27D8b3F8C97D69908b5E284","bsc"]
SZN = ["SZN","SZN_USDT","TDxL4V5LE6TYSFXSCWJkkSsCYbgmrDnTer","tron"]
SIREN = ["SIREN","SIREN_USDT","0x997A58129890bBdA032231A52eD1ddC845fc18e1","bsc"]
BR = ["BR","BR_USDT","0xFf7d6A96ae471BbCD7713aF9CB1fEeB16cf56B41","bsc"]
BUBB = ["BUBB","BUBB_USDT","0xd5369a3CaC0f4448A9A96bb98AF9c887c92fC37B","bsc"]
TAT = ["TAT","TAT_USDT","0x996D1b997203a024E205069a304161ba618d1c61","bsc"]
AFT = ["AFT","AFT_USDT","0xaBd834A7823567673e1Ac07635d5D9857b34A8d3","bsc"]
APX = ["APX","APX_USDT","0x78F5d389F5CDCcFc41594aBaB4B0Ed02F31398b3","bsc"]
BOME = ["AFT","BOME_USDC","ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82","solana"]
ETHFI = ["ETHFI","ETHFI_USDC","0x7189fb5B6504bbfF6a852B13B7B82a3c118fDc27","arbitrum"]
XRP = ["XRP","XRP_USDC","0xb9Ce0dd29C91E02d4620F57a66700Fc5e41d6D15","cronos"]
PEPE = ["PEPE","PEPE_USDC","0x6982508145454Ce325dDbE47a25d4ec3d2311933","ethereum"]
TRUMP = ["TRUMP","TRUMP_USDC","6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN","solana"]
ENA = ["ENA","ENA_USDC","0x57e114B691Db790C35207b2e685D4A43181e6061","ethereum"]
PARTI = ["PARTI","PARTI_USDT","0x59264f02D301281f3393e1385c0aEFd446Eb0F00","base"]
TIBBIR = ["TIBBIR","TIBBIR_USDT","0xA4A2E2ca3fBfE21aed83471D28b6f65A233C6e00","base"]

tokens=[DHN,A8,JUP,DOGINME,MUBARAK,TUT,FORM,SZN,SIREN,BR,BUBB,TAT,AFT,APX,BOME,ETHFI,XRP,PEPE,TRUMP,ENA,PARTI,TIBBIR]
tasks = []

async def bot_loop(chat_id):
    c=0
    conds = [False]*len(tokens)
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="MEXC", url="https://futures.mexc.com/ru-RU/exchange/KET_USDT")]
    ])
    mexc_fut,dex_price,spreds=[],[],[]*len(tokens)
    while True:
        c=0
        mexc_fut,dex_price,spreds,tasks=[],[],[],[]
        for num in range(len(tokens)):
            try:
                mexc_fut_value = asyncio.create_task(mexc.get_futures_mexc_price(tokens[num][1]))
                dex_price_value = asyncio.create_task(ds.GetDexScreenerPrice(tokens[num][3], tokens[num][2]))
  
                tasks.append(mexc_fut_value)
                tasks.append(dex_price_value)
            except:
                pass
        results = await asyncio.gather(*tasks)
        for result in results:
            mexc_fut.append(result) if c%2==0 else dex_price.append(result)	
            c+=1
        
       

        for num in range(len(tokens)):
            try:
                spreds.append(round(100 - ((float(mexc_fut[num])/float(dex_price[num]))*100), 5))
                print("{",mexc_fut[num], dex_price[num], spreds[num],"}  ",end="")

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
            except:
                spreds.append(None)
                print("{",mexc_fut[num], dex_price[num], None,"}  ",end="")

                
        print("   ")


        await asyncio.sleep(delay)
    
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
