from datetime import datetime
from sqlite3 import Date
from uuid import uuid4
import inquirer

from Movement import Movement
from Volumes import Volumes


class Workout:
    
    def __init__(
        self,
        date: datetime,
        duration: str,
        cals: float,
        split: str,
        movement_count: int
    ) -> None:

        # Basic workout data
        self.id = uuid4()
        self.date = date
        self.duration = duration
        self.cals = cals
        self.split = split

        # Custom workout data
        self.movements: list[Movement] = Movement.builder(movement_count, self.id)
        self.volumes: Volumes = Volumes.builder(self.movements, self.id)

    # Converts to an item that pandas will turn into a DataFrame
    def to_dict(self):
        return {
            'id': [self.id],
            'date': [self.date],
            'duration': [self.duration],
            'cals': [self.cals],
            'split': [self.split]
        }
    
    # Aggregates all the prompts into a single method call
    @classmethod
    def builder(cls, movement_count: int):
        questions = [
            inquirer.Text('time', message="When did you workout? (HH:MM)"),
            inquirer.Text('duration', message="How long did you workout? (MM:SS)"),
            inquirer.Text('cals', message="Active calories burned: "),
            inquirer.List(
                'split',
                message='Choose a split: ',
                choices=['upper', 'lower', 'full'],
            ),
        ]
        answers = inquirer.prompt(questions)
        date_conversion = datetime.strptime(f'{Date.today()} {answers["time"]}', '%Y-%m-%d %H:%M')
        return Workout(date_conversion,
                       answers['duration'],
                       answers['cals'],
                       answers['split'],
                       movement_count)
    
