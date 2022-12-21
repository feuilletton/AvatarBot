from pyrogram import Client
import asyncio
from icmplib import ping
import os
from dotenv import load_dotenv


load_dotenv()
user_ip = os.getenv('USER_IP')

def pinger():
    if ping(user_ip).is_alive:
        return True
    else:
        return False


async def change_avatar(app):
    if pinger():
        print('Online')
        await app.set_profile_photo(photo="downloads/on.png")
        await delete_prev_avatar(app)

    else:
        print('Offline')
        await app.set_profile_photo(photo="downloads/off.png")
        await delete_prev_avatar(app)


async def delete_prev_avatar(app):
    prev_avatar = [p async for p in app.get_chat_photos("me")]
    prev_avatar = prev_avatar[1].file_id
    await app.delete_profile_photos(prev_avatar)

