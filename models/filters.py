from aiogram import Bot
from aiogram.filters import Filter
from aiogram.enums import ChatMemberStatus
from aiogram.types import Message

async def is_admin(message: Message, bot: Bot, member_id: int):
    try:
        chat_member = await bot.get_chat_member(message.chat.id, member_id)
        return chat_member.status in [ChatMemberStatus.CREATOR, ChatMemberStatus.ADMINISTRATOR]
    except:
        return False

class IsAdmin(Filter):
    async def __call__(self, message: Message, bot: Bot) -> bool:
        try:
            if not await is_admin(message, bot, bot.id):
                await message.reply("Я не могу так делать без админки")
                return False
            if not await is_admin(message, bot, message.from_user.id):
                await message.reply("Эта команда доступна только администраторам")
                return False
            return True
        except:
            return False

class IsReplyAndAdmin(Filter):
    async def __call__(self, message: Message, bot: Bot) -> bool:
        try:
            if not await is_admin(message, bot, bot.id):
                await message.reply("Я не могу так делать без админки")
                return False
            if not message.reply_to_message:
                await message.reply("Нужно отметить сообщение")
                return False
            if not await is_admin(message, bot, message.from_user.id):
                await message.reply("Эта команда доступна только администраторам")
                return False
            if await is_admin(message, bot, message.reply_to_message.from_user.id):
                await message.reply("Нельзя сделать это с администратором")
                return False
            return True
        except:
            return False