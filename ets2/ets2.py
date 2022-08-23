from ast import expr_context
from cgi import print_arguments
import os
from datetime import datetime
from fileinput import filename
import time
from googletrans import Translator
import re
import pickle
from ets2.chat_message import ChatMessage

from discord import Discord
# print(webhookURL)
translator = Translator()


class Ets():
    def __init__(self):
        # Get latest chat log file
        try:
            logsPath = os.path.expanduser('~\Documents') + "\ETS2MP\logs"
            chatLogFiles = [os.path.join(logsPath, x) for x in os.listdir(
                logsPath) if x.endswith(".txt") and x.startswith("chat_")]
            self.newestChatLogFile = max(chatLogFiles, key=os.path.getctime)
            print(self.newestChatLogFile)
        except:
            print("No chat log files found")
        # self.chatLogPath = r'C:\Users\LOCKhart\Documents\ETS2MP\logs\chat_2022_08_13_log.txt'
        self.cache_last_line = 'Connection established!'
        self.discord = Discord()

    def tail(self):
        filename = self.newestChatLogFile
        with open(filename, "rb") as file:
            try:
                file.seek(-2, os.SEEK_END)
                while file.read(1) != b'\n':
                    file.seek(-2, os.SEEK_CUR)
            except OSError:
                file.seek(0)
            last_line = file.readline().decode()
            return last_line

    def translateMessage(self, sendToDiscord=True):
        last_line = self.tail()
        tmpID = r"^.+\(.*\): "
        try:
            with open('cache_last_line.pkl', 'rb') as file:
                self.cache_last_line = pickle.load(file)
        except:
            print("No pickle file/ Running for the first time")
        if last_line != self.cache_last_line:
            chat_message = ChatMessage(last_line)
            try:
                # Remove timestamp
                translated = chat_message.translate_message()
                print(translated)
                if sendToDiscord:
                    self.discord.send_message(translated)
                self.cache_last_line = last_line
                with open('cache_last_line.pkl', 'wb') as file:
                    pickle.dump(self.cache_last_line, file)
                return translated

            except Exception as e:
                print("exception :",e)
                if sendToDiscord:
                    self.discord.send_message(last_line[11:])
                print(last_line[11:])
                self.cache_last_line = last_line
                with open('cache_last_line.pkl', 'wb') as file:
                    pickle.dump(self.cache_last_line, file)
                return '!!!!!!!!!!!!!!!     ' + last_line

        return "No new chat message"
