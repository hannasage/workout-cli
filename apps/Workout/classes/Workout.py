from datetime import datetime

from numpy import append

from apps.Workout.classes.Movement import Movement

class Workout: 
    
    def __init__(self, 
                date,
                duration, 
                cals, 
                split, 
                total_vol, 
                ch_vol, 
                bi_vol,
                tri_vol, 
                shld_vol,
                bk_vol, 
                core_vol, 
                qd_vol, 
                ham_vol, 
                cf_vol) -> None:
        self.date = date
        self.duration = duration
        self.cals = cals
        self.split = split
        self.total_vol = total_vol
        self.ch_vol = ch_vol
        self.bi_vol = bi_vol
        self.tri_vol = tri_vol
        self.shld_vol = shld_vol
        self.bk_vol = bk_vol
        self.core_vol = core_vol
        self.qd_vol = qd_vol
        self.ham_vol = ham_vol
        self.cf_vol = cf_vol

    # Enumerate class callsign
    def callsign():
        return 'workout'

    # Converts to an item that pandas will turn into a DataFrame
    def to_dict(self):
        return {
            'date': [self.date],
            'duration': [self.duration],
            'calse': [self.cals],
            'split': [self.split],
            'total_vol': [self.total_vol],
            'ch_vol': [self.ch_vol],
            'bi_vol': [self.bi_vol],
            'tri_vol': [self.tri_vol],
            'shld_vol': [self.shld_vol],
            'back_vol': [self.bk_vol],
            'core_vol': [self.core_vol],
            'quad_vol': [self.qd_vol],
            'ham_vol': [self.ham_vol],
            'cf_vol': [self.cf_vol]
        }
    
    # Prompts the user for the column name passed in
    def prompt(column_header):
        return input(f'Enter {column_header}: ')
    
    # Aggregates all the prompts into a single method call
    def create(self):
        date = datetime.strptime(self.prompt('date like Jan 01 2022 18:30'), '%b %d %Y %H:%M')
        duration = self.prompt('duration in MM:SS')
        cals = self.prompt('total calories')
        split = self.prompt('split (upper/lower)')
        movements = self.capture_movements(self)
        print(movements[0].volume)
        
        return Workout(date,
                        duration,
                        cals,
                        split)
    
    def capture_movements(self):
        movements = []
        count = int(input('How many movements did you do?: '))
        i = 0
        while i < count:
            name = self.prompt('Movement name')
            group = self.prompt('Muscle group')
            sets = self.prompt('Sets')
            reps = self.prompt('Reps')
            weight = self.prompt('Total weight')
            movements.append(
                Movement(
                    group,
                    name,
                    reps,
                    sets,
                    weight
                )
            )
            i += 1
        return movements
