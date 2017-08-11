from unittest import TestCase
from assertpy import assert_that

from generator.FileIO import FileIO


class TestFileIO(TestCase):
    def __init__(self, methodName='runTest'):
        self.test_file_uri = "..\content\TestFile.cs"
        super().__init__(methodName)

    def tearDown(self):
        FileIO.delete(self.test_file_uri)

    def test_read(self):
        result = FileIO.read("..\content\ExampleFile.cs")
        assert_that(result).is_not_none()

    def test_write(self):
        test_content = "testContent"
        FileIO.write(self.test_file_uri, test_content)
        result = FileIO.read(self.test_file_uri)
        assert_that(result).is_equal_to(test_content)

    def test_delete(self):
        test_content = "testContent"
        FileIO.write(self.test_file_uri, test_content)
        FileIO.delete(self.test_file_uri)
        with self.assertRaises(FileNotFoundError):
            FileIO.read(self.test_file_uri)
