import re
from googletrans import Translator
from ets2.exceptions.unable_to_translate import UnableToTranslate


class ChatMessage():
    """Stores indivual log messages"""
    message: str
    REGEX_STR = r"^.+\(.*\): "

    def __init__(self, message: str) -> None:
        self.translator = Translator()
        self.message = message.strip()

    def translate_message(self) -> str:
        """Translate message using google translate

        Raises UnableToTranslate if message cannot be translated
        """
        if (self.get_user_message_prefix() is not None):
            message_prefix: str = self.get_user_message_prefix().group()
            message_sufix: str = self.message.split(message_prefix)[1]
            translated = message_prefix + \
                str(self.translator.translate(message_sufix, dest='en').text)
            return translated
        else:
            raise UnableToTranslate()

    def get_user_message_prefix(self):
        """Get message prefix object according to regex

        If the given message is a user chat message will return a regex match object
        """
        message_prefix = re.search(self.REGEX_STR, self.message)
        if (message_prefix is not None):
            return message_prefix
        return None
