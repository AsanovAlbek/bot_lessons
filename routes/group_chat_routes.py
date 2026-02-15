from datetime import datetime, timedelta

from aiogram import Router, Bot
from aiogram.types import Message, ChatPermissions, ChatMemberUpdated
from aiogram.filters import Command, ChatMemberUpdatedFilter, IS_MEMBER, IS_NOT_MEMBER, IS_ADMIN
from models.filters import IsReplyAndAdmin, IsAdmin

group_chat_router = Router(name="group_chat_router")

@group_chat_router.message(Command("delete"), IsReplyAndAdmin())
async def delete(message: Message):
    await message.reply_to_message.delete()
    await message.answer("Сообщение удалено!")

@group_chat_router.message(Command("mute"), IsReplyAndAdmin())
async def mute(message: Message, bot: Bot):
    await bot.restrict_chat_member(
        chat_id=message.chat.id,
        user_id=message.reply_to_message.from_user.id,
        until_date=datetime.now() + timedelta(minutes=1),
        permissions=ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_other_messages=False,
            can_send_polls=False
        ),
    )
    await message.answer(f"Пользователь {message.reply_to_message.from_user.username} молчит на минуту")

@group_chat_router.message(Command("unmute"), IsReplyAndAdmin())
async def unmute(message: Message, bot: Bot):
    await bot.restrict_chat_member(
        chat_id=message.chat.id,
        user_id=message.reply_to_message.from_user.id,
        permissions=ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_polls=True,
            can_send_other_messages=True,
        )
    )

@group_chat_router.message(Command("kick"), IsReplyAndAdmin())
async def kick(message: Message, bot: Bot):
    await bot.ban_chat_member(
        chat_id=message.chat.id,
        user_id=message.reply_to_message.from_user.id,
        until_date=datetime.now() + timedelta(seconds=5),
    )
    await message.answer(f"Пользователь {message.reply_to_message.from_user.username} кикнут")

@group_chat_router.message(Command("ban"), IsReplyAndAdmin())
async def ban(message: Message, bot: Bot):
    await bot.ban_chat_member(
        chat_id=message.chat.id,
        user_id=message.reply_to_message.from_user.id,
    )
    await message.answer(f"Пользователь {message.reply_to_message.from_user.username} забанен")

@group_chat_router.message(Command("unban"), IsReplyAndAdmin())
async def unban(message: Message, bot: Bot):
    await bot.unban_chat_member(
        chat_id=message.chat.id,
        user_id=message.reply_to_message.from_user.id,
        only_if_banned=True
    )
    await message.answer(f"Пользователь {message.reply_to_message.from_user.username} разбанен")

@group_chat_router.message(Command("only_admin"), IsAdmin())
async def mute_all_not_admins(message: Message, bot: Bot):
    await bot.set_chat_permissions(
        chat_id=message.chat.id,
        permissions=ChatPermissions(
            can_send_messages=False,  # Запрещаем писать всем
            can_send_media_messages=False,
            can_send_polls=False,
            can_send_other_messages=False,
            can_add_web_page_previews=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False
        )
    )
    await message.answer("Теперь писать могут только админы")

@group_chat_router.message(Command("all_can_write"), IsAdmin())
async def all_can_write(message: Message, bot: Bot):
    await bot.set_chat_permissions(
        chat_id=message.chat.id,
        permissions=ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_polls=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True,
            can_change_info=False,
            can_invite_users=True,
            can_pin_messages=False
        )
    )
    await message.answer("Снова все могут писать")

@group_chat_router.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
async def welcome_chat_member(event: ChatMemberUpdated, bot: Bot):
    await bot.send_message(event.chat.id, f"Салам алейкум, {event.new_chat_member.user.full_name}")

@group_chat_router.chat_member(ChatMemberUpdatedFilter(IS_MEMBER >> IS_NOT_MEMBER))
async def bye_chat_member(event: ChatMemberUpdated, bot: Bot):
    await bot.send_message(event.chat.id, f"Ну и уходи, {event.new_chat_member.user.full_name}")

@group_chat_router.chat_member(ChatMemberUpdatedFilter(IS_MEMBER >> IS_ADMIN))
async def make_admin_chat_member(event: ChatMemberUpdated, bot: Bot):
    await bot.send_message(event.chat.id, f"{event.new_chat_member.user.full_name} коронован!")