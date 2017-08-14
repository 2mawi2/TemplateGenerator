from unittest import TestCase

from gen.utils import file_utils


class TestFiles(TestCase):
    def test_get_full_path(self):
        print(file_utils.get_full_path())
