from pyrogram import Client, filters
from dotenv import load_dotenv
import additional.addcandle as addcandle
import os


load_dotenv()

my_id = os.getenv('MY_USER_ID')

@Client.on_message(filters.photo)
async def photos(Client, message):
    if '/change_on' in message.caption and str(message.from_user.id) == str(my_id):
        await Client.download_media(message.photo.file_id, file_name='on.png')
    elif '/change_off' in message.caption and str(message.from_user.id) == str(my_id):
        await Client.download_media(message.photo.file_id, file_name='off.png')
    elif '/create_off' in message.caption and str(message.from_user.id) == str(my_id):
        await Client.download_media(message.photo.file_id, file_name='off.png')
        addcandle.analyze('downloads/off.png')
        await message.reply_document(document='downloads/off.png', quote=True)


@Client.on_message(filters.text)
async def text(Client, message):
    if '/get_session_string' in message.text and str(message.from_user.id) == str(my_id):
        print(await Client.export_session_string())
    elif '/get_user_id' in message.text:
        print(message.from_user.id)
    elif '/get_current_off' in message.text:
        await message.reply_document(document='downloads/off.png', quote=True)

