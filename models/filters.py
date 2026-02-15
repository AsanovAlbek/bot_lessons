from aiogram import F, Bot
from aiogram.filters import Filter
from aiogram.enums import ChatMemberStatus
from aiogram.types import Message, User

async def is_admin(message: Message, bot: Bot, user: User):
    chat_member = await bot.get_chat_member(message.chat.id, user.id)
    return chat_member.status in [ChatMemberStatus.CREATOR, ChatMemberStatus.ADMINISTRATOR]

class IsAdmin(Filter):
    async def __call__(self, message: Message, bot: Bot) -> bool:
        is_user_admin = await is_admin(message, bot, message.from_user)
        if not is_user_admin:
            await message.reply("Эта команда доступна только администраторам")
        return is_user_admin

class IsReplyAndAdmin(Filter):
    async def __call__(self, message: Message, bot: Bot) -> bool:
        if not message.reply_to_message:
            await message.reply("Нужно отметить сообщение")
            return False
        if not await is_admin(message, bot, message.from_user):
            await message.reply("Эта команда доступна только администраторам")
            return False
        if not await is_admin(message, bot, message.reply_to_message.from_user):
            await message.reply("Нельзя сделать это с администратором")
            return False
        return True