from models import SessionLocal, User
from random import randint
from sqlalchemy import select


async def insert_new_user_in_table(user_tg_id: int, name: str):
    async with SessionLocal() as session:
        query = await session.execute(
            select(User).filter(User.user_id == user_tg_id))
        print(f"{query=}")
        user = query.scalar()
        print(f"{user=}")
        if not user:
            secret_number = randint(6, 100)
            new_user = User(
                user_id=user_tg_id, user_name=name, secret_number=secret_number
            )
            session.add(new_user)
        await session.commit()


async def update_and_return_attempts(user_tg_id: int, us_number: int):
    async with SessionLocal() as session:
        query = await session.execute(
            select(User).filter(User.user_id == user_tg_id))
        user = query.scalar()
        if user:
            user.attempts -= 1
            attempts = user.attempts
            await session.commit()
            return attempts


async def reset(user_tg_id: int):
    async with SessionLocal() as session:
        query = await session.execute(
            select(User).filter(User.user_id == user_tg_id))
        user = query.scalar()
        if user:
            user.attempts = 5
            await session.commit()
