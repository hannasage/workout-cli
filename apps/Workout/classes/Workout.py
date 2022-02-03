from datetime import datetime
from uuid import uuid4
import pandas as pd
import inquirer

from apps.Workout.classes.Movement import Movement

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
            'date': [self.date],
            'duration': [self.duration],
            'calse': [self.cals],
            'split': [self.split],
            'total_vol': [self.volumes.total_vol],
            'ch_vol': [self.volumes.chest_vol],
            'bi_vol': [self.volumes.bicep_vol],
            'tri_vol': [self.volumes.tricep_vol],
            'shld_vol': [self.volumes.shoulder_vol],
            'back_vol': [self.volumes.back_vol],
            'core_vol': [self.volumes.core_vol],
            'quad_vol': [self.volumes.quad_vol],
            'ham_vol': [self.volumes.hammy_vol],
            'cf_vol': [self.volumes.calf_vol]
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
    
