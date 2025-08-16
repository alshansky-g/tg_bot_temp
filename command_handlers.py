from aiogram import Router
from aiogram.filters import CommandStart
from lexicon import start_greeting
from aiogram.types import Message, ReplyKeyboardRemove
from external_funcs import insert_new_user_in_table


command_router = Router()


@command_router.message(CommandStart())
async def start_command(message: Message):
    print(f'Пользователь {message.chat.first_name} запустил бота')
    user_name = message.chat.first_name or 'Без имени'
    if message.from_user:
        user_tg_id = message.from_user.id
        await insert_new_user_in_table(user_tg_id, user_name)
    await message.answer(
        f'Привет, {user_name}! \U0001F60a\n {start_greeting}',
        reply_markup=ReplyKeyboardRemove()
    )
    print('Процесс старта бота завершен')