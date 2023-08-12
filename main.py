from pyrogram import Client, filters
from dotenv import load_dotenv
import TelegramBot as TG
import logging
import os

load_dotenv()

From_Channel = int(os.getenv('FROM_CHANNEL'))
To_Channels = [int(channel) for channel in os.getenv("TO_CHANNELS").replace(" ", "").split(",")]

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
app_name = os.getenv('APP_NAME')

app = Client(app_name, api_id, api_hash)

logging.basicConfig(filename=f'{app_name}.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.getLogger().addHandler(logging.StreamHandler())

@app.on_message(filters.chat(From_Channel) & filters.text)
async def text_without_photo_handler(client, message):
    for channel in To_Channels:
        # This line is for sending with user account.
        # await client.copy_message(channel, From_Channel, message.message_id)

        # This lines are for sending with bot account.
        TG.send_message(message=message.text, chat_id=str(channel), parse_mode='HTML') # This line is for sending with bot account.

@app.on_message(filters.chat(From_Channel) & filters.photo)
async def text_with_photo_handler(client, message):
    for channel in To_Channels:
        # This line is for sending with user account.
        # await client.copy_message(channel, From_Channel, message.message_id)

        # This lines are for sending with bot account.
        photo_path = await message.download()
        TG.send_photo(photo_path=photo_path, caption=message.caption, chat_id=str(channel), parse_mode='HTML')
        os.remove(photo_path)

def main():
    app.run()

if __name__ == '__main__':
    try:
        logging.info(f"Start: {app_name} started.")
        main()
    except KeyboardInterrupt:
        logging.info("Exit: Bot stopped by user.")
        exit()
    except Exception as e:
        logging.error(f"Error: {e}")
        main()