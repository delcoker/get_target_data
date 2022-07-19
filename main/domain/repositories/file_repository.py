from pandas import DataFrame
from main.domain.services.enums.file_type import FileType


class FileRepository:
    def insert(self, file_name):
        pass

    def find(self, file_path: str, file_type: FileType) -> DataFrame:
        pass

    def update(self, file_path):
        pass

    def delete(self, file_path):
        pass
