import os
from datetime import datetime
from fileinput import filename
import time
from googletrans import Translator
import re

from discord import Discord
# print(webhookURL)
translator = Translator()


class Ets():
    def __init__(self):
        self.now = datetime.now()
        self.chatLogPath = os.path.expanduser(
            '~\Documents') + "\ETS2MP\logs" + "\chat_" + self.now.strftime("%Y_%m_%d") + "_log.txt"
        # self.chatLogPath = r'C:\Users\LOCKhart\Documents\ETS2MP\logs\chat_2022_08_13_log.txt'
        self.cache_last_line = 'Connection established!'
        self.discord = Discord()

    def tail(self):
        filename = self.chatLogPath
        with open(filename, "rb") as file:
            try:
                file.seek(-2, os.SEEK_END)
                while file.read(1) != b'\n':
                    file.seek(-2, os.SEEK_CUR)
            except OSError:
                file.seek(0)
            last_line = file.readline().decode()
            return last_line

    def translateMessage(self, sendToDiscord = False):
        last_line = self.tail()
        # print(last_line)
        # print(self.cache_last_line)
        tmpID = r"^.+\(.*\): "
        if last_line != self.cache_last_line:
            try:
                spliStri = re.search(tmpID, last_line)
                prequel = spliStri.group()
                sequel = last_line.split(spliStri.group())
                translated = str(
                    prequel) + str(translator.translate(sequel[1], dest='en').text)
                # Remove timestamp
                translated = translated[11:]
                print(translated)
                if sendToDiscord:
                    self.discord.send_message(translated)
                self.cache_last_line = last_line
                return translated

            except Exception as e:
                print(e)
                if sendToDiscord:
                    self.discord.send_message(last_line[11:])
                print(last_line[11:])
                self.cache_last_line = last_line
                return '!!!!!!!!!!!!!!!     ' + last_line

        return "No new chat message"

def main():
    ets = Ets()
    try:
        last_line = ets.tail()
    except:
        print("No log file found")
        exit()

    while (True):
        ets.translateMessage(True)


if __name__ == "__main__":
    main()
