from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
from models.keyboards import start_keyboard
from texts import help_text

command_router = Router(name="command_router")

@command_router.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Салам, {message.from_user.first_name}!", reply_markup=start_keyboard())

@command_router.message(Command("bomber"))
async def bomber(message: Message, command: CommandObject):
    try:
        count, msg = command.args.split(maxsplit=1)
        for _ in range(int(count)):
            await message.answer(msg)
    except ValueError:
        await message.answer("Неверный формат. Пример: /bomber 10 Хакуна матата")

@command_router.message(Command("calc"))
async def calculator(message: Message, command: CommandObject):
    await message.answer(f"Ваш ответ: {eval(command.args)}")

@command_router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(help_text, parse_mode="HTML")