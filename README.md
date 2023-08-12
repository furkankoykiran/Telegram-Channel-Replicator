# Telegram-Channel-Replicator
This is a Telegram bot developed using the Pyrogram library that forwards(replicates) messages from one channel (X) to multiple other channels (A, B, C) based on specified conditions. The bot can handle both text and photo messages. You should edit `.env` file to set your bot token and channel ids.
## Example Multiple Channel
```env
TO_CHANNELS = -1001234567890, -1001234567890, -1001234567890
```
## Windows Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
## Linux Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Run
```python
python main.py
```