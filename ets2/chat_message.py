import re
from googletrans import Translator
from ets2.exceptions.unable_to_translate import UnableToTranslate


class ChatMessage():
    """Stores indivual log messages"""
    message: str
    REGEX_STR = r"^.+\(.*\): "

    def __init__(self, message: str, debug: bool = False) -> None:
        self.translator = Translator()
        self.message = message.strip()
        self.debug = debug
        if self.debug:
            print("Message is:", self.message)

    def translate_message(self) -> str:
        """Translate message using google translate

        Raises UnableToTranslate if message cannot be translated
        """
        if (self.get_user_message_prefix() == None):
            raise UnableToTranslate()
        message_prefix: str = self.get_user_message_prefix().group()
        message_sufix: str = self.message.split(message_prefix)[1]
        translated = message_prefix + \
            str(self.translator.translate(message_sufix, dest='en').text)
        if self.debug:
            print("Translated message: ", translated)
        return translated

    def get_user_message_prefix(self):
        """Get message prefix object according to regex

        If the given message is a user chat message will return a regex match object
        """
        message_prefix = re.search(self.REGEX_STR, self.message)
        if self.debug:
            print("Message prefix is: ", message_prefix)
        return message_prefix
