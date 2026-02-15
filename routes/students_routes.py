from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from models.keyboards import groups_keyboard
from storage.storage import get_all_groups
from models.fsm import FindStudentState
from aiogram.fsm.context import FSMContext

students_router = Router(name="students_router")
groups = get_all_groups()

@students_router.message(F.text == "Группы IT TOP")
async def student_message(message: Message):
    await message.answer("Группы колледжа IT TOP", reply_markup=groups_keyboard())

@students_router.message(F.text == "Найти студента")
async def start_find_student(message: Message, state: FSMContext):
    await message.answer("Введите имя студента")
    await state.set_state(FindStudentState.wait_name)

@students_router.message(FindStudentState.wait_name, F.text)
async def find_student_by_name(message: Message, state: FSMContext):
    results = []
    for group, students in groups.items():
        for student in students:
            if message.text.lower() in student.lower():
                results.append((student, group))
    if not results:
        await message.answer("Студент не найден")
    else:
        result = [f"{n}. {student[0]} из {student[1]}" for n, student in enumerate(results, start=1)]
        await message.answer("\n".join(result))
    await state.clear()

@students_router.callback_query(F.data.in_(groups))
async def group_handler(query: CallbackQuery):
    global groups
    group = groups[query.data]
    group = [f"{num}. {student}" for num, student in enumerate(group, start=1)]
    await query.message.answer("\n".join(group))