from aiogram.dispatcher.filters.state import State, StatesGroup

class MessageState(StatesGroup):
    message = State()
    confirm = State()

class DeleteVideoState(StatesGroup):
    code = State()
    confirm = State()

    