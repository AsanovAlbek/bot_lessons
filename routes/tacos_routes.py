from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from models.callbacks import TacosCallbackData, TacosNavCallback, TacosNavAction
from models.keyboards import tacos_keyboard
from storage.storage import get_tacos_menu

tacos_router = Router(name="tacos_router")
page = 1
limit = 5

@tacos_router.message(F.text == "Хочу такос")
async def tacos_message(message: Message):
    await message.answer("Выбирай братуха", reply_markup=tacos_keyboard(page, limit))

@tacos_router.callback_query(TacosCallbackData.filter())
async def select_tacos(query: CallbackQuery, callback_data: TacosCallbackData):
    await query.message.answer(f"Вы выбрали {callback_data.name} по цене {callback_data.price}")

@tacos_router.callback_query(TacosNavCallback.filter())
async def navigate_tacos(query: CallbackQuery, callback_data: TacosNavCallback):
    global page
    if callback_data.action in [TacosNavAction.NEXT, TacosNavAction.BACK]:
        page = callback_data.page
    else:
        await query.answer()
        return

    total_pages = (len(get_tacos_menu()) + limit - 1) // limit
    page = max(1, min(page, total_pages))

    await query.message.edit_text(
        "Выбирай братуха",
        reply_markup=tacos_keyboard(page, limit)
    )
    await query.answer()