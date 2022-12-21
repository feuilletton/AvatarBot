from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()

bot_path = os.getenv('BOT_PATH')

os.chdir(bot_path)

def analyze(image):
    image = Image.open(image)
    w, h = image.size
    if w + h != 1400:
        done_image = image.resize((700, 700))
        create_avatar(done_image)
    else:
        create_avatar(image)

def create_avatar(image):
    image = image.convert('RGBA')
    candle = Image.open('additional/candle.png')
    new_avatar = Image.new('RGBA', image.size)
    new_avatar = Image.alpha_composite(new_avatar, image)
    new_avatar = Image.alpha_composite(new_avatar, candle)
    new_avatar.save('downloads/off.png')






