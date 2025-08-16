from aiogram import Router
from filters import DATA_IS_DIGIT
from lexicon import answer, no_att_lost, new_game
from aiogram.types import Message
from external_funcs import reset, update_table, check_attempts_lost_number
import asyncio


game_router = Router()

@game_router.message(DATA_IS_DIGIT())
async def process_numbers_answer(message: Message):
    if message.from_user:
        user_tg_id = message.from_user.id
        user_name = message.chat.first_name

    if await check_attempts_lost_number(user_tg_id):
        print(f'\n Попыток для {user_name} = 0. Игра завершена.')
        await reset(user_tg_id)
        await message.answer(text=f'{user_name} {answer}')
        await asyncio.sleep(1)
        await message.answer(text=no_att_lost)
        await message.answer(text=new_game)
    else:
        await update_table(user_tg_id, int(message.text))
        print('Вроде обновили таблицу')
        await message.answer(text=f'{user_name} {answer}')