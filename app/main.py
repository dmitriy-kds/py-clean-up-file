import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        pass

    def __exit__(self, *args) -> None:
        os.remove(self.filename)
