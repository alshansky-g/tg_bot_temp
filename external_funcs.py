from models import SessionLocal, User
from random import randint
from sqlalchemy import select


async def insert_new_user_in_table(user_tg_id: int, name: str):
    async with SessionLocal() as session:
        query = await session.execute(
            select(User).filter(User.user_id == user_tg_id))
        print(f"{query=}")
        needed_data = query.scalar()
        print(f"{needed_data=}")
        if not needed_data:
            secret_number = randint(6, 100)
            new_user = User(
                user_id=user_tg_id, user_name=name, secret_number=secret_number
            )
            session.add(new_user)
        await session.commit()


async def update_table(user_tg_id: int, us_number: int):
    async with SessionLocal() as session:
        query = await session.execute(
            select(User).filter(User.user_id == user_tg_id))
        n = query.scalar()
        print(n)
        if n:
            n.attempts -= 1
            if n.att_1 == 0:
                n.att_1 = us_number
            elif n.att_2 == 0:
                n.att_2 = us_number
            elif n.att_3 == 0:
                n.att_3 = us_number
            elif n.att_4 == 0:
                n.att_4 = us_number
            elif n.att_5 == 0:
                n.att_5 = us_number
            await session.commit()


async def check_attempts_lost_number(user_tg_id: int):
    async with SessionLocal() as session:
        query = await session.execute(
            select(User).filter(User.user_id == user_tg_id))
        user = query.scalar()
        if user:
            print("\n\nОсталось попыток ", user.attempts)
            if user.attempts == 1:
                return True
            return False


async def reset(user_tg_id: int):
    async with SessionLocal() as session:
        query = await session.execute(
            select(User).filter(User.user_id == user_tg_id))
        user = query.scalar()
        if user:
            user.attempts = 5
            user.att_1 = user.att_2 = user.att_3 = user.att_4 = user.att_5 = 0
            await session.commit()
