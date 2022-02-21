from sqlite3 import Date
import pandas as pd

from .Enums import *


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

    # Enumerate class callsign
    def callsign(self):
        return 'nutrition'

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

    # Prompts the user for the column name passed in
    def prompt(column_header, measure):
        return input(f'Enter {column_header} ({measure}): ')

    # Aggregates all the prompts into a single method call
    @classmethod
    def create(self, workout_id=None):
        cals = self.prompt(NutritionEnums.CALS.value, Units.KCAL.value)
        protein = self.prompt(NutritionEnums.PROTEIN.value, Units.GRAM.value)
        carbs = self.prompt(NutritionEnums.CARBS.value, Units.GRAM.value)
        fiber = self.prompt(NutritionEnums.FIBER.value, Units.GRAM.value)
        sugars = self.prompt(NutritionEnums.SUGARS.value, Units.GRAM.value)
        fats = self.prompt(NutritionEnums.FATS.value, Units.GRAM.value)
        sat_fats = self.prompt(NutritionEnums.SAT_FATS.value, Units.GRAM.value)
        unsat_fats = self.prompt(NutritionEnums.UNSAT_FATS.value, Units.GRAM.value)
        chol = self.prompt(NutritionEnums.CHOL.value, Units.MG.value)
        sodium = self.prompt(NutritionEnums.SODIUM.value, Units.MG.value)
        potassium = self.prompt(NutritionEnums.POTASSIUM.value, Units.MG.value)
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
