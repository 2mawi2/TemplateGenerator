import os


class FileIO:
    @staticmethod
    def read(file: str):
        with open(file, "r") as f:
            return f.read()

    @staticmethod
    def delete(file: str):
        if os.path.isfile(file):
            os.remove(file)

    @staticmethod
    def write(file: str, content: str):
        with open(file, "w+") as f:
            f.write(content)

    @classmethod
    def exists(cls, file):
        return os.path.isfile(file)
