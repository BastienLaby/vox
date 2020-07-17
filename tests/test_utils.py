from unittest import TestCase

from vox.utils import show_message


class TestUtils(TestCase):

    def test_show_message(self):
        show_message("hello")
