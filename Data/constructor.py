import json


class DataStorage:
    def init(self):
        self.__file_path = "file.json"
        self.status = "disconnected"
        self.content = None

    @property
    def file_path(self):
        return self.__file_path

    def _create_storage(self):
        with open(self.__file_path, "w") as self.__my_file:
            json.dump([], self.__my_file)
            return self.__my_file

    def connect(self):
        try:
            self.__my_file = open(self.file_path, "r")
            self.content = json.load(self.__my_file)
            self.status = "connected"
            return self.__my_file
        except FileNotFoundError:
            return self._create_storage()

    def disconnect(self):
        if self.status == "connected":
            self.__my_file.close()
            self.status = "disconnected"
            print("File was closed")


class DataStorageWrite(DataStorage):
    def connect(self):
        super().connect()

    def _create_storage(self):
        super()._create_storage()

    def append(self, file):
        if self.status == "connected":
            self.content.append(file)
            with open(self.file_path, "w") as self.__my_file:
                json.dump(self.content, self.__my_file)
            print("Text was added")


my_file = DataStorageWrite()
my_file.connect()
my_file.append("Write any text")
my_file.disconnect()
print(my_file.content)