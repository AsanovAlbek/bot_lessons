from aiogram import Bot, Dispatcher
from aiogram.types import BotCommandScopeDefault, BotCommandScopeAllChatAdministrators
import asyncio
from routes.all_routers import all_routers
from models.commands import commands, admin_commands
from os import getenv
from dotenv import load_dotenv

dp = Dispatcher()

async def main():
    load_dotenv()
    bot = Bot(token=getenv("TOKEN"))
    dp.include_routers(*all_routers)
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands, BotCommandScopeDefault())
    await bot.set_my_commands(admin_commands, BotCommandScopeAllChatAdministrators())
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())