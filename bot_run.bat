@echo off

call %~dp0New_Telegram_bot\venv\Scripts\activate

cd %~dp0New_Telegram_bot


set TOKEN=5369416528:AAGOHJl_HWt8VDic0BaQajAGZPPIyYpC7XE

python Bot_Telegram.py

pause