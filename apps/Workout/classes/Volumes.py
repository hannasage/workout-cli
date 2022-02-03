from uuid import UUID
from .Movement import Movement
from .Enums import Volume_Enums

class Volumes:

    def __init__(self, movements: list[Movement], workout_id: UUID) -> None:
        self.workout_id = workout_id
        self.chest_vol = 0
        self.bicep_vol = 0
        self.tricep_vol = 0
        self.shoulder_vol = 0
        self.back_vol = 0
        self.core_vol = 0
        self.quad_vol = 0
        self.hammy_vol = 0
        self.calf_vol = 0
        self.total_vol = 0

        self.calculate_volumes(movements)

    def to_dict(self):
        return{
            'workout_id': [self.workout_id],
            'total_vol': [self.total_vol],
            'ch_vol': [self.chest_vol],
            'bi_vol': [self.bicep_vol],
            'tri_vol': [self.tricep_vol],
            'shld_vol': [self.shoulder_vol],
            'back_vol': [self.back_vol],
            'core_vol': [self.core_vol],
            'quad_vol': [self.quad_vol],
            'ham_vol': [self.hammy_vol],
            'cf_vol': [self.calf_vol]
        }

    def calculate_volumes(self, movements: list[Movement]):
        for mv in movements:
            # TODO: WHY ARE THESE TUPLES?
            volume = mv.sets[0] * mv.reps[0] * mv.total_weight
            if mv.group == Volume_Enums.CHEST:
                self.chest_vol += volume
            elif mv.group == Volume_Enums.BICEP:
                self.bicep_vol += volume
            elif mv.group == Volume_Enums.TRICEP:
                self.tricep_vol += volume
            elif mv.group == Volume_Enums.SHOULDER:
                self.shoulder_vol += volume
            elif mv.group == Volume_Enums.BACK:
                self.back_vol += volume
            elif mv.group == Volume_Enums.CORE:
                self.core_vol += volume
            elif mv.group == Volume_Enums.QUADS:
                self.quad_vol += volume
            elif mv.group == Volume_Enums.HAMSTRINGS:
                self.hammy_vol += volume
            elif mv.group == Volume_Enums.CALF:
                self.calf_vol += volume
            else:
                pass
            # Add to total
            self.total_vol += volume
    
    def builder(movements: list[Movement], workout_id: UUID):
        return Volumes(movements, workout_id)

