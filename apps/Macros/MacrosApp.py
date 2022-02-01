from apps.Macros.classes.Macros import Macros
from functions.CreateEntry import create_entry

class MacrosApp:

    def __init__(self) -> None:
        self.path = 'C:\Projects\workout-cli\data\macros-log.csv'

    def add_new_entry(self):
        return create_entry(self.path, Macros)
        