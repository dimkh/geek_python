class StorageError(Exception):

    def __init__(self, txt):
        self.txt = txt
