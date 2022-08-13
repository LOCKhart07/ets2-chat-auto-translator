from discord_webhook import DiscordWebhook
from dotenv import load_dotenv
import os



class Discord():
    def __init__(self) :
        load_dotenv()
        self.webhookUrl = os.getenv('WEBHOOK_URL')
    
    def send_message(self,translated):
        webhook = DiscordWebhook(url=self.webhookUrl, content=translated)
        response = webhook.execute()