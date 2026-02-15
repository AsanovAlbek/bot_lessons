from aiogram.filters.callback_data import CallbackData
from enum import Enum

class TacosNavAction(Enum):
    BACK = "back"
    NEXT = "next"
    IGNORE = "ignore"

class TacosCallbackData(CallbackData, prefix="tacos"):
    name: str
    price: float

class TacosNavCallback(CallbackData, prefix="tacos_nav"):
    action: TacosNavAction
    page: int = 1