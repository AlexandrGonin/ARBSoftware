import sys
sys.path.append("dex screener")
sys.path.append("mexc")
import dex_screener_api as ds
import mexc_api as mexc

import asyncio
import logging
import time
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.markdown import bold
import aiogram.utils.markdown as fmt

logging.basicConfig(level=logging.INFO)
bot = Bot(token="YOUR TG BOT TOKEN")
dp = Dispatcher()


chat_id=("YOUR CHAT ID (GROUP WITH FRIEND FOR EXAMPLE)")

KET = ["KET", "KET_USDT", "0xFFFF003a6BAD9b743d658048742935fFFE2b6ED7", "avalanche"]

DHN = ["DHN", "DHN_USDT", "0x32462bA310E447eF34FF0D15BCE8613aa8C4A244", "ethereum", "https://dexscreener.com/ethereum/0x1dcd41a3876959023ef49603374af655973a64cf"]
A8 = ["A8", "A8_USDT", "0x3E5A19c91266aD8cE2477B91585d1856B84062dF", "ethereum", "https://dexscreener.com/ethereum/0x0e59f2cfda2bb2e7fee10278dd2016a2e4311d72"]
JUP = ["JUP", "JUP_USDT", "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN", "solana", "https://dexscreener.com/solana/c1mglojnlwbkadvu9bhdtgzz1ozx4dz5zgdgcgvvw8wz"]
DOGINME = ["DOGINME","DOGINME_USDT","0x6921B130D297cc43754afba22e5EAc0FBf8Db75b","base", "https://dexscreener.com/base/0xade9bcd4b968ee26bed102dd43a55f6a8c2416df"]
MUBARAK = ["MUBARAK","MUBARAK_USDT","0x5C85D6C6825aB4032337F11Ee92a72DF936b46F6","bsc", "https://dexscreener.com/bsc/0x90a54475d512b8f3852351611c38fad30a513491"]
TUT = ["TUT","TUT_USDT","0xCAAE2A2F939F51d97CdFa9A86e79e3F085b799f3","bsc", "https://dexscreener.com/bsc/0x6dafbf0ab4fd72e2a5c0ad5a1ed277d3bf8a8d1f"]
FORM = ["FORM","FORM_USDT","0x5b73A93b4E5e4f1FD27D8b3F8C97D69908b5E284","bsc", "https://dexscreener.com/bsc/0x7cb113b487e025b3a69537fca579559433240cb5"]
SZN = ["SZN","SZN_USDT","TDxL4V5LE6TYSFXSCWJkkSsCYbgmrDnTer","tron", "https://dexscreener.com/tron/tlkhsbpybgq4a7neuac4cyxmhizjuks9ox"]
SIREN = ["SIREN","SIREN_USDT","0x997A58129890bBdA032231A52eD1ddC845fc18e1","bsc", "https://dexscreener.com/bsc/0xb2af49dbf526054faf19602860a5e298a79f3d05"]
BR = ["BR","BR_USDT","0xFf7d6A96ae471BbCD7713aF9CB1fEeB16cf56B41","bsc", "https://dexscreener.com/bsc/0xf95f84e2bad9c234f93dd66614b82f9a854b452e"]
BUBB = ["BUBB","BUBB_USDT","0xd5369a3CaC0f4448A9A96bb98AF9c887c92fC37B","bsc", "https://dexscreener.com/bsc/0xc8255e3fa0f4c6e6678807d663f9e2263e23a8e8"]
TAT = ["TAT","TAT_USDT","0x996D1b997203a024E205069a304161ba618d1c61","bsc", "https://dexscreener.com/bsc/0x71cd938b95ad63cb724b986bd7628558a6af5bb1"]
AFT = ["AFT","AFT_USDT","0xaBd834A7823567673e1Ac07635d5D9857b34A8d3","bsc", "https://dexscreener.com/bsc/0xa06261529e36f7f702e2c9764905e27f93237286"]
APX = ["APX","APX_USDT","0x78F5d389F5CDCcFc41594aBaB4B0Ed02F31398b3","bsc", "https://dexscreener.com/solana/2nffx4fk4k98paqpyjly9trsvfahj8ctxfhh4yceb43g"]
BOME = ["AFT","BOME_USDC","ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82","solana", "https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt"]
ETHFI = ["ETHFI","ETHFI_USDC","0x7189fb5B6504bbfF6a852B13B7B82a3c118fDc27","arbitrum", "https://dexscreener.com/arbitrum/0x7e9cb8ad4a7683070e233f3eb1d07d87272b9b26"]
XRP = ["XRP","XRP_USDC","0xb9Ce0dd29C91E02d4620F57a66700Fc5e41d6D15","cronos", "https://dexscreener.com/cronos/0xe83ffad6c8cec615b7a8d7c96706f717e91784d2"]
PEPE = ["PEPE","PEPE_USDC","0x6982508145454Ce325dDbE47a25d4ec3d2311933","ethereum", "https://dexscreener.com/ethereum/0xa43fe16908251ee70ef74718545e4fe6c5ccec9f"]
PARTI = ["PARTI","PARTI_USDT","0x59264f02D301281f3393e1385c0aEFd446Eb0F00","base", "https://dexscreener.com/bsc/0xc0fb39f705ee65ef098dd5452997a7846d156aa9"]
TIBBIR = ["TIBBIR","TIBBIR_USDT","0xA4A2E2ca3fBfE21aed83471D28b6f65A233C6e00","base", "https://dexscreener.com/base/0x0c3b466104545efa096b8f944c1e524e1d0d4888"]

TRUMP = ["TRUMP","TRUMP_USDC","6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN","solana", "https://dexscreener.com/solana/hkujrp5tyqlbeudjkwjgnhs2957qkjr2iwhjkttma1xs"]
ENA = ["ENA","ENA_USDC","0x57e114B691Db790C35207b2e685D4A43181e6061","ethereum", "https://dexscreener.com/ethereum/0xc3db44adc1fcdfd5671f555236eae49f4a8eea18"]
BNBCARD = ["BNBCARD", "BNBCARD", ]

tokens=[DHN,A8,JUP,DOGINME,MUBARAK,TUT,FORM,SZN,SIREN,BR,BUBB,TAT,AFT,APX,BOME,ETHFI,XRP,PEPE,PARTI,TIBBIR,  TRUMP,ENA] 
tasks = []

if sys.platform == 'win32':
	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def bot_loop(chat_id):
    delay = 2.5
    c=0
    conds=[0]*len(tokens)

    mexc_fut,dex_price,spreds=[],[],[]*len(tokens)
    while True:
        print(" _____________________________________________________ ")
        print("|                                                      |")
        c=0
        mexc_fut,dex_price,spreds,tasks=[],[],[],[]
        for num in range(len(tokens)):
            try:
                mexc_fut_value = asyncio.create_task(mexc.get_futures_mexc_price(tokens[num][1]))
                dex_price_value = asyncio.create_task(ds.GetDexScreenerPrice(tokens[num][3], tokens[num][2]))
  
                tasks.append(mexc_fut_value)
                tasks.append(dex_price_value)
            except:
                print(12345)
        results = await asyncio.gather(*tasks)
        for result in results:
            mexc_fut.append(result) if c%2==0 else dex_price.append(result)	
            c+=1

        for num in range(len(tokens)):
            keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="MEXC", url=f"https://futures.mexc.com/ru-RU/exchange/{tokens[num][1]}"), types.InlineKeyboardButton(text="DEX", url=tokens[num][4])]])
            try:        
                spreds.append(round(100 - ((float(mexc_fut[num])/float(dex_price[num]))*100), 5))
            except:
                spreds.append(0)
            print("TOKEN:",tokens[num][0]," {",mexc_fut[num], dex_price[num], spreds[num],"}  ")
            if spreds[num] < -5 and conds[num] == 0:
                await bot.send_message(chat_id,
                    fmt.text(
                        fmt.text(fmt.hbold("Token: ", tokens[num][0])),
                        fmt.text(fmt.hbold("MEXC Futures"), mexc_fut[num]),
                        fmt.text(fmt.hbold("DEX Screener"), dex_price[num]),
                        fmt.text(fmt.hbold("Спред: "),  spreds[num]),
                        fmt.text(fmt.hbold("Открыть short")),
                        sep="\n\n",), parse_mode="HTML", reply_markup=keyboard)  
                conds[num] = 1
            elif (spreds[num] > -1.5 and conds[num] != 0) or spreds[num] == None:
                await bot.send_message(chat_id,
                    fmt.text(
                        fmt.text(fmt.hbold("Token: ", tokens[num][0])),
                        fmt.text(fmt.hbold("MEXC Futures"), mexc_fut[num]),
                        fmt.text(fmt.hbold("DEX Screener"), dex_price[num]),
                        fmt.text(fmt.hbold("Спред: "),  spreds[num]),
                        fmt.text(fmt.hbold("Закрыть short")),
                        sep="\n\n",), parse_mode="HTML", reply_markup=keyboard)
                conds[num] = 0



                
        print("|_____________________________________________________|")
        time.sleep(delay)
    
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
