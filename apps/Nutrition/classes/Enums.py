from enum import Enum

class Units(Enum):
    GRAM = 'g'
    MG = 'mg'
    KCAL = 'kcal'

class Helpers(Enum):
    KEY = 'key',
    VALUE = 'value'

"""
    EnumWithHelpers serves as a parent object all enums can extend to receive
    additional utility specific to this application.
"""
class EnumWithHelpers(Enum):

    @classmethod
    def property_as_string_list(cls, desired_value):
        properties_list = []
        for item in cls:
            if desired_value == Helpers.KEY:
                properties_list.append(item.name)
            elif desired_value == Helpers.VALUE:
                properties_list.append(item.value)
            else:
                raise PropertyTypeError(desired_value)
        return properties_list


class NutritionEnums(EnumWithHelpers):
    CALS = 'cals'
    PROTEIN = 'protein'
    CARBS = 'carbs'
    FIBER = 'fiber'
    SUGARS = 'sugars'
    FATS = 'fats'
    SAT_FATS = 'saturated fats'
    UNSAT_FATS = 'unsaturated fats'
    CHOL = 'cholesterol'
    SODIUM = 'sodium'
    POTASSIUM = 'potassium'


# Custom error type because why not?
class PropertyTypeError(Exception):

    def __init__(
            self,
            given_property
    ):
        self.message = f'{given_property} is not of type \'key\' or \'value\''
