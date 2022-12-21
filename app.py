from pyrogram import Client
import os
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import additional.pingpong as pingpong


### load env.
load_dotenv()
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
session_string = os.getenv('SESSION_STRING')

### setup
plugins = dict(root='plugins')

if session_string:
    app = Client('Account', session_string=session_string, plugins=plugins)
else:
    app = Client('Account', api_id, api_hash, plugins=plugins)

scheduler = AsyncIOScheduler()

### Check online/change avatar
async def onliner():
    await pingpong.change_avatar(app)


### Start app
scheduler.add_job(onliner, "interval", seconds=30)
scheduler.start()
app.run()
