from aiogram.types import BotCommand

commands = [
    BotCommand(command="start", description="Запуск"),
    BotCommand(command="calc", description="Калькулятор"),
    BotCommand(command="bomber", description="Бомбер"),
    BotCommand(command="help", description="Помощь")
]

admin_commands = [
    *commands,
    BotCommand(command="mute", description="Заткнуть (на минуту)"),
    BotCommand(command="unmute", description="Разрешить говорить"),
    BotCommand(command="ban", description="Бан"),
    BotCommand(command="unban", description="Разбан"),
    BotCommand(command="kick", description="Кикнуть"),
    BotCommand(command="delete", description="Удалить сообщение"),
    BotCommand(command="only_admin", description="Писать могут только админы"),
    BotCommand(command="all_can_write", description="Все могут писать"),
]