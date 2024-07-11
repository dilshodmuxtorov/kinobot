from aiogram.dispatcher.filters.state import State, StatesGroup

class CodeState(StatesGroup):
    waiting_for_code = State()