class UnableToTranslate(Exception):
    def __init__(self):
        super().__init__("Unable to translate message")
