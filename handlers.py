import json

from aiogram import types, Router
from aiogram.filters import Command, CommandObject
import aiohttp
import os
basic_router = Router()



@basic_router.message(Command('start'))
async def handler(message: types.Message, command: CommandObject):
    token: str = command.args
    session = aiohttp.ClientSession()
    back_request_url = f'{os.environ.get("BACKEND_ADDRESS")}tg/connect'
    data={"user": message.from_user.username, "token": token}
    result = await session.post(url=back_request_url, data=json.dumps(data))
    if result   .status == 200:
        await message.answer("Авторизация прошла успешно, вы можете возвращаться обратно на страницу.")
    else:
        await message.answer("Произошла непредвиденная ошибка при попытке авторизации.")
    await session.close()

