from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from models.callbacks import TacosCallbackData, TacosNavCallback, TacosNavAction
from storage.storage import get_all_groups, get_tacos_menu

def start_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Группы IT TOP")
    builder.button(text="Найти студента")
    builder.button(text="Хочу такос")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

def groups_keyboard():
    builder = InlineKeyboardBuilder()
    for group in get_all_groups():
        builder.button(text=group, callback_data=group)
    return builder.as_markup(resize_keyboard=True)

def tacos_keyboard(page: int = 1, limit: int = 5):
    menu = get_tacos_menu()
    start = (page - 1) * limit
    end = min(start + limit, len(menu))
    items = menu[start:end]
    total_pages = (len(menu) + limit - 1) // limit
    builder = InlineKeyboardBuilder()
    for menu_item in items:
        builder.button(
            text=menu_item["name"],
            callback_data=TacosCallbackData(
                name=menu_item["name"],
                price=menu_item["price"],
            )
        )
    nav_buttons = []
    if page > 1:
        nav_buttons.append(
            InlineKeyboardButton(
                text="Назад",
                callback_data=TacosNavCallback(action=TacosNavAction.BACK, page=page - 1).pack()
            )
        )
    nav_buttons.append(
        InlineKeyboardButton(
            text=f"{page}/{total_pages}",
            callback_data=TacosNavCallback(action=TacosNavAction.IGNORE, page=page).pack()
        )
    )
    if page < total_pages:
        nav_buttons.append(
            InlineKeyboardButton(
                text="Вперед",
                callback_data=TacosNavCallback(action=TacosNavAction.NEXT, page=page + 1).pack()
            )
        )
    builder.adjust(1)
    builder.row(*nav_buttons)
    return builder.as_markup()
