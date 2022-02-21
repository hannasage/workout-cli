from uuid import UUID
from Movement import Movement
from Enums import VolumeEnums


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
            if mv.group == VolumeEnums.CHEST.value:
                self.chest_vol += volume
            elif mv.group == VolumeEnums.BICEP.value:
                self.bicep_vol += volume
            elif mv.group == VolumeEnums.TRICEP.value:
                self.tricep_vol += volume
            elif mv.group == VolumeEnums.SHOULDER.value:
                self.shoulder_vol += volume
            elif mv.group == VolumeEnums.BACK.value:
                self.back_vol += volume
            elif mv.group == VolumeEnums.CORE.value:
                self.core_vol += volume
            elif mv.group == VolumeEnums.QUADS.value:
                self.quad_vol += volume
            elif mv.group == VolumeEnums.HAMSTRINGS.value:
                self.hammy_vol += volume
            elif mv.group == VolumeEnums.CALF.value:
                self.calf_vol += volume
            else:
                pass
            # Add to total
            self.total_vol += volume
    
    def builder(self, movements: list[Movement], workout_id: UUID):
        return Volumes(movements, workout_id)

