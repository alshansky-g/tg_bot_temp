from aiogram import Router
from filters import DATA_IS_DIGIT
from lexicon import answer, no_att_lost, new_game
from aiogram.types import Message
from external_funcs import reset, update_and_return_attempts
import asyncio


game_router = Router()

@game_router.message(DATA_IS_DIGIT())
async def process_numbers_answer(message: Message):
    if message.from_user:
        user_tg_id = message.from_user.id
        user_name = message.chat.first_name

    if await update_and_return_attempts(user_tg_id, int(message.text)):
            await message.answer(text=f'{user_name} {answer}')
    else:
        await reset(user_tg_id)
        await message.answer(text=f'{user_name} {answer}')
        await asyncio.sleep(1)
        await message.answer(text=no_att_lost)
        await message.answer(text=new_game)
