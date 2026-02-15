from aiogram import Router
from aiogram.types import Message

fallback_router = Router(name="fallback_router")

@fallback_router.message()
async def fallback_handler(message: Message):
    await message.answer("Неизвестное действие")