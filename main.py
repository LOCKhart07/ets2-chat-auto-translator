import os
from datetime import datetime
from fileinput import filename
import time
from discord_webhook import DiscordWebhook
from googletrans import Translator
import re
from dotenv import load_dotenv
load_dotenv()
webhookURL = os.getenv('WEBHOOK_URL')
print(webhookURL)
translator = Translator()

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

now = datetime.now()
# chatLogPath = os.path.expanduser('~\Documents') + "\ETS2MP\logs" + "\chat_" + now.strftime("%Y_%m_%d") + "_log.txt"
chatLogPath = r'C:\Users\LOCKhart\Documents\ETS2MP\logs\chat_2022_08_12_log.txt'

cache_last_line = 'Connection established!'
tmpID = r"^.+\(.*\): "

# check if log file exists
try:
    tail(chatLogPath)
except:
    print("No log file found")
    exit()

while(True):
    last_line = tail(chatLogPath)
    if last_line != cache_last_line:
        try:
            spliStri = re.search(tmpID, last_line)
            prequel = spliStri.group()
            sequel = last_line.split(spliStri.group())
            translated = str(prequel) + str(translator.translate(sequel[1],dest = 'en').text)
            webhook = DiscordWebhook(url=webhookURL,
                                    content=translated)
            response = webhook.execute()
            print(translated)
            cache_last_line = last_line
        except:
            print('!!!!!!!!!!!!!!!     ' + last_line)
            cache_last_line = last_line


