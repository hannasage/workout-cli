from datetime import datetime
from uuid import uuid4
import pandas as pd
import inquirer

from .Movement import Movement
from .Volumes import Volumes


class Workout: 
    
    def __init__(self, 
                 date: datetime,
                 duration: str, 
                 cals: float, 
                 split: str,
                 movement_count: int) -> None:

        # Basic workout data
        self.id = uuid4()
        self.date = date
        self.duration = duration
        self.cals = cals
        self.split = split

        # Custom workout data
        self.movements: list[Movement] = Movement.builder(movement_count, self.id)
        self.volumes: Volumes = Volumes.builder(self.movements, self.id)

    # Enumerate class callsign
    def callsign():
        return 'workout'

    # Converts to an item that pandas will turn into a DataFrame
    # TODO: This holds over for the volumes dataframe but eventually
    #       I see this being handled by a Framer class; it takes a
    #       Workout and creates DataFrame shapes for any dataframe!
    def to_dict(self):
        return {
            'id': [self.id],
            'date': [self.date],
            'duration': [self.duration],
            'calse': [self.cals],
            'split': [self.split]
        }
    
    # Aggregates all the prompts into a single method call
    def builder(movement_count: int):
        questions = [
            inquirer.Text('date', message="Today's Date (in Jan 01 2022 17:30 format): "),
            inquirer.Text('duration', message="Workout duration (mm:ss): "),
            inquirer.Text('cals', message="Active calories burned: "),
            inquirer.List(
                'split',
                message='Choose a split: ',
                choices=['upper', 'lower', 'full'],
            ),
        ]
        answers = inquirer.prompt(questions)
        date_conversion = datetime.strptime(answers['date'], '%b %d %Y %H:%M')
        return Workout(date_conversion,
                       answers['duration'],
                       answers['cals'],
                       answers['split'],
                       movement_count)
    
