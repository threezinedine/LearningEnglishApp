import os
from .i_database import IDatabase
from ..file import create_folder_if_not_exist, get_list_file_paths
from ..date import get_k_previous_date


class Database(IDatabase):
    base_folder = "database"

    def __init__(self):
        today_folder = get_k_previous_date()
        self.__folder = os.path.join(self.base_folder, today_folder)     
        create_folder_if_not_exist(self.__folder)

    @property
    def folder(self):
        return self.__folder

    def load(self, date):
        pass
