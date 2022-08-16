import pytest
import unittest
from ets2.chat_message import ChatMessage
from ets2.exceptions.unable_to_translate import UnableToTranslate


class TestChatMessage():
    CHAT_STRING_1 = "[20:34:04] [MPI] Kamisato Ayaka (1092): mau ke calaais?"
    CHAT_STRING_1_WS = "  [20:34:04] [MPI] Kamisato Ayaka (1092): mau ke calaais? "
    CHAT_STRING_1_PREFIX = "[20:34:04] [MPI] Kamisato Ayaka (1092): "
    CHAT_STRING_1_TRANSLATED = "[20:34:04] [MPI] Kamisato Ayaka (1092): is the calaais still?"
    CHAT_STRING_2 = "[20:32:53] [System] Player suayp (1378) has been kicked"
    SYSTEM_2 = "[00:14:04] [System] Player gli4121 (265) has been kicked"

    def test_removes_whitespace_around(self):
        """ check if whitespace is removed"""
        chat_message = ChatMessage(self.CHAT_STRING_1_WS)
        assert chat_message.message == self.CHAT_STRING_1

    def test_get_user_message_prefix(self):
        """ message prefix works for chat message"""
        chat_message = ChatMessage(self.CHAT_STRING_1)
        assert chat_message.get_user_message_prefix().group() == self.CHAT_STRING_1_PREFIX

    def test_user_message_prefix_2(self):
        """ message prefix is None for system message"""
        chat_message = ChatMessage(self.CHAT_STRING_2)
        assert chat_message.get_user_message_prefix() is None
        chat_message = ChatMessage(self.SYSTEM_2)
        assert chat_message.get_user_message_prefix() is None

    def test_translate_works_on_user_message(self):
        """ translate works """
        chat_message = ChatMessage(self.CHAT_STRING_1)
        assert chat_message.translate_message() == self.CHAT_STRING_1_TRANSLATED

    def test_translate_does_not_work_on_system_message(self):
        """ translate does not work for system message """
        chat_message = ChatMessage(self.CHAT_STRING_2)
        with pytest.raises(UnableToTranslate, match="Unable to translate message"):
            chat_message.translate_message()
