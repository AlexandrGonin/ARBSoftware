import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Ваш токен бота
API_TOKEN = "8031545073:AAFppT7ziBlV3vpkn9zflITk_GmPnLSYpDY"

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот, который покажет тебе ID твоего чата.")

# Обработчик любых сообщений
@dp.message()
async def show_chat_id(message: types.Message):
    # Получаем ID чата
    chat_id = message.chat.id
    await message.reply(f"Твой ID чата: {chat_id}")

# Основная функция запуска бота
async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())