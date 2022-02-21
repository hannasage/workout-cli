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


class VolumeEnums(EnumWithHelpers):
    CHEST = 'chest'
    BICEP = 'bicep'
    TRICEP = 'tricep'
    SHOULDER = 'shoulder'
    BACK = 'back'
    CORE = 'core'
    QUADS = 'quads'
    HAMSTRINGS = 'hamstrings'
    CALF = 'calf'


class ChestMovements(EnumWithHelpers):
    CB_FLY = 'cable fly'
    DB_PRESS = 'db chest press'
    DB_FLY = 'db fly'
    DB_PRESS_INCL = 'incline db chest press'


class BicepMovements(EnumWithHelpers):
    CHIN_UP = 'chin up'
    DB_CURL = 'db curl'
    DB_HAMMER = 'db hammer curl'
    DB_INCL_CURL = 'db incline curl'
    DB_INCL_HAMMER = 'db incline hammer curl'
    CB_HAMMER = 'cable hammer curl'


class TricepMovements(EnumWithHelpers):
    DB_TRI_PRESS = 'db tri press'
    DB_FLOOR_PRESS = 'db floor press'
    DB_TRI_KICKBACK = 'db tri kickback'
    DB_TRI_EXT = 'db tri extension'
    CB_TRI_PULL = 'cable tri pulldown'


class ShoulderMovements(EnumWithHelpers):
    DB_LAT_RAISE = 'db lateral raise'
    DB_DELT_RAISE = 'db delt raise'
    DB_FRONT_RAISE = 'db front raise'
    DB_SHLD_PRESS = 'db shoulder press'
    CB_FACE_PULL = 'cable face pull'
    CB_LAT_RAISE = 'cable lateral raise'


class BackMovements(EnumWithHelpers):
    CB_LAT_PULL = 'cable lat pulldown'
    CB_ROW = 'cable row'
    DB_SHRUGS = 'db shrugs'
    DB_ROW = 'db row'
    DB_UP_ROW = 'db upright row'
    PULL_UP = 'pull up'


class CoreMovements(EnumWithHelpers):
    CRUNCH = 'crunches'
    CB_AXES = 'cable axes'


class QuadMovements(EnumWithHelpers):
    SQUAT = 'squat'
    LUNGE = 'lunges'
    LUNGE_WALK = 'walking lunges'
    STEP_UPS = 'step ups'


class HamMovements(EnumWithHelpers):
    RDL = 'rdl'
    SL_RDL = 'single-leg rdl'
    CB_PULL_THRU = 'cable pull through'
    HIP_THRUST = 'hip thrust'


class CalfMovements(EnumWithHelpers):
    CALF_RAISE = 'calf raises'


# Custom error type because why not?
class PropertyTypeError(Exception):

    def __init__(
            self,
            given_property
    ):
        self.message = f'{given_property} is not of type \'key\' or \'value\''
