from sqlite3 import Date

from Enums import *


class Nutrition:

    def __init__(
            self,
            workout_id,
            cals,
            protein,
            carbs,
            fiber,
            sugars,
            fats,
            sat_fats,
            unsat_fats,
            chol,
            sodium,
            potassium
    ) -> None:
        self.workout_id = workout_id
        self.date = Date.today()
        self.cals = cals
        self.protein = protein
        self.carbs = carbs
        self.fiber = fiber
        self.sugars = sugars
        self.fats = fats
        self.sat_fats = sat_fats
        self.unsat_fats = unsat_fats
        # Convert from mg -> g
        self.chol = int(chol) / 1000
        self.sodium = int(sodium) / 1000
        self.potassium = int(potassium) / 1000

    # Converts to an item that pandas will turn into a DataFrame
    def to_dict(self):
        return {
            'workout_id': [self.workout_id],
            'date': [self.date],
            'calories': [self.cals],
            'protein': [self.protein],
            'carbs': [self.carbs],
            'fiber': [self.fiber],
            'sugars': [self.sugars],
            'fats': [self.fats],
            'sat_fats': [self.sat_fats],
            'unsat_fats': [self.unsat_fats],
            'chol': [self.chol],
            'sodium': [self.sodium],
            'potassium': [self.potassium]
        }

    # Aggregates all the prompts into a single method call
    @classmethod
    def builder(cls, workout_id=None):
        cals = prompt(NutritionEnums.CALS.value, Units.KCAL.value)
        protein = prompt(NutritionEnums.PROTEIN.value, Units.GRAM.value)
        carbs = prompt(NutritionEnums.CARBS.value, Units.GRAM.value)
        fiber = prompt(NutritionEnums.FIBER.value, Units.GRAM.value)
        sugars = prompt(NutritionEnums.SUGARS.value, Units.GRAM.value)
        fats = prompt(NutritionEnums.FATS.value, Units.GRAM.value)
        sat_fats = prompt(NutritionEnums.SAT_FATS.value, Units.GRAM.value)
        unsat_fats = prompt(NutritionEnums.UNSAT_FATS.value, Units.GRAM.value)
        chol = prompt(NutritionEnums.CHOL.value, Units.MG.value)
        sodium = prompt(NutritionEnums.SODIUM.value, Units.MG.value)
        potassium = prompt(NutritionEnums.POTASSIUM.value, Units.MG.value)
        return Nutrition(
            workout_id,
            cals,
            protein,
            carbs,
            fiber,
            sugars,
            fats,
            sat_fats,
            unsat_fats,
            chol,
            sodium,
            potassium
        )


# Prompts the user for the column name passed in
def prompt(column_header, measure):
    return input(f'Enter {column_header} ({measure}): ')
