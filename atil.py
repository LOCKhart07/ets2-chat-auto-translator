from fileinput import filename
import os
import time
import requests
from discord_webhook import DiscordWebhook


def tail(filename):
    with open(filename, "rb") as file:
        try:
            file.seek(-2, os.SEEK_END)
            while file.read(1) != b'\n':
                file.seek(-2, os.SEEK_CUR)
        except OSError:
            file.seek(0)
        last_line = file.readline().decode()
        return last_line


cache_last_line = '[20:12:48] Connection established!'
while (True):
    last_line = tail(r"C:\Users\LOCKhart\Documents\ETS2MP\logs\chat_2022_08_12_log.txt")
    if last_line != cache_last_line:
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1007656272566423572/ZYKeFkbpCwm2VbRnZNW2rQvirZiuHbwNMDuO5CUcCDydvhLesE4sdI8I1DnZrUW4F9xx',
                                content=last_line)
        response = webhook.execute()
        print("last_line")
        cache_last_line = last_line
