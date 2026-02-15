from aiogram.fsm.state import State, StatesGroup

class FindStudentState(StatesGroup):
    wait_name = State()