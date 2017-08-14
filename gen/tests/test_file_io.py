from unittest import TestCase

from assertpy import assert_that

from gen.file_generator.file_io import FileIO
from gen.utils import test_utils


class TestFileIO(TestCase):
    def __init__(self, methodName='runTest'):
        self.test_file = test_utils.test_file_uri
        super().__init__(methodName)

    def tearDown(self):
        FileIO.delete(self.test_file)

    def test_read(self):
        result = FileIO.read(test_utils.example_template_uri)
        assert_that(result).is_not_none()

    def test_write(self):
        test_content = "testContent"
        FileIO.write(self.test_file, test_content)
        result = FileIO.read(self.test_file)
        assert_that(result).is_equal_to(test_content)

    def test_delete(self):
        test_content = "testContent"
        FileIO.write(self.test_file, test_content)
        FileIO.delete(self.test_file)
        with self.assertRaises(FileNotFoundError):
            FileIO.read(self.test_file)

    def test_exists(self):
        test_content = "testContent"
        FileIO.write(self.test_file, test_content)
        result = FileIO.exists(self.test_file)
        assert_that(result).is_true()
