
from numpy import double


class Movement:

    def __init__(self,
                muscle_group,
                name,
                reps,
                sets,
                total_weight) -> None:
        self.muscle_group = muscle_group
        self.name = name
        self.reps = int(reps),
        self.sets = int(sets),
        self.total_weight = float(total_weight)
        self.volume = int(reps) * int(sets) * float(total_weight)

