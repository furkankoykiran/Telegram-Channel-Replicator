from dotenv import load_dotenv
import requests
import os

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

def send_message(message=None, reply_to_msg_id=None, parse_mode='HTML', chat_id=None):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    while True:
        try:
            if reply_to_msg_id is None:
                params = {
                    "chat_id": chat_id,
                    "text": message,
                    "parse_mode": parse_mode,
                    "disable_web_page_preview": True
                }
            else:
                params = {
                    "chat_id": chat_id,
                    "text": message,
                    "reply_to_message_id": reply_to_msg_id,
                    "parse_mode": parse_mode,
                    "disable_web_page_preview": True
                }
            response = requests.get(url, params=params)
            
            if response.status_code == 200:
                result = response.json()
                message_id = result['result']['message_id']
                break
            else:
                print(response.text)
                return None
        except Exception as e:
            print("Error:", e)
            return None
        
    return message_id

def send_photo(photo_path=None, caption=None, chat_id=None, reply_to_msg_id=None, parse_mode='HTML'):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    while True:
        try:
            with open(photo_path, 'rb') as photo:
                params = {
                    "chat_id": chat_id,
                    "caption": caption,
                    "parse_mode": parse_mode,
                    "disable_web_page_preview": True
                }

                if reply_to_msg_id is not None:
                    params["reply_to_message_id"] = reply_to_msg_id

                files = {'photo': photo}
                response = requests.post(url, params=params, files=files)

                if response.status_code == 200:
                    result = response.json()
                    message_id = result['result']['message_id']
                    break
                else:
                    print(response.text)
                    return None
        except Exception as e:
            print("Error:", e)
            return None
    
    return message_id