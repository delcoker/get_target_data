from main.domain.exceptions.FileTypeUnsupportedException import FileTypeUnsupportedException
# from main.domain.exceptions import FileTypeUnsupportedException
from main.domain.repositories.file_repository import FileRepository
from main.domain.services.enums.file_type import FileType

import awswrangler as wr


class FileRepositoryImpl(FileRepository):
    def __init__(self):
        pass

    def insert(self, file_name):
        pass

    def find(self, file_path: str, file_type: FileType):
        if file_type == FileType.CSV:
            return wr.s3.read_csv(file_path, error_bad_lines=False)
        if file_type == FileType.EXCEL:
            return wr.s3.read_excel(file_path, error_bad_lines=False)
        raise FileTypeUnsupportedException(message="File type is unsupported!!")

    def update(self, file_path):
        pass

    def delete(self, file_path):
        pass
