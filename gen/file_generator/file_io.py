import os


class FileIO:
    @staticmethod
    def read(file: str) -> str:
        with open(file, "r") as f:
            return f.read()

    @staticmethod
    def delete(file: str) -> None:
        if os.path.isfile(file):
            os.remove(file)

    @staticmethod
    def write(file: str, content: str) -> None:
        with open(file, "w+") as f:
            f.write(content)

    @staticmethod
    def exists(file) -> bool:
        return os.path.isfile(file)
