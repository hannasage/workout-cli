from .Movement import Movement
from .Enums import Volume_Enums

class Volumes:

    def __init__(self, movements: list[Movement]) -> None:
        self.chest_vol = 0
        self.bicep_vol = 0
        self.tricep_vol = 0
        self.shoulder_vol = 0
        self.back_vol = 0
        self.core_vol = 0
        self.quad_vol = 0
        self.hammy_vol = 0
        self.calf_vol = 0
        self.calculate_volumes(movements)
        self.total_vol = self.calc_total_vol(self)

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
    
    def builder():
        count = int(input('How many movements did you do?: '))
        movements = Movement.builder(count)
        return Volumes(movements)
    
    def calc_total_vol(self):
        return sum(
            [
                self.chest_vol,
                self.bicep_vol,
                self.tricep_vol,
                self.shoulder_vol,
                self.back_vol,
                self.core_vol,
                self.quad_vol,
                self.hammy_vol,
                self.calf_vol,
            ]
        )
