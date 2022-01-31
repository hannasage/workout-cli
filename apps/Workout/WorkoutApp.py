from classes.Workout import Workout
from functions.CreateEntry import create_entry

class WorkoutApp:

    def __init__(self) -> None:
        self.path = 'C:\Projects\workout-cli\data\workout-log.csv'

    def add_new_entry(self):
        return create_entry(self.path, Workout)
        