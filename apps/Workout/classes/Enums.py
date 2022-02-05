from enum import Enum


class Helpers(Enum):
    KEY = 'key',
    VALUE = 'value'


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
    DB_PRESS = 'db chest press'
    DB_FLY = 'db fly'
    DB_PRESS_INCL = 'incline db chest press'


class BicepMovements(EnumWithHelpers):
    CHIN_UP = 'chin up'
    DB_CURL = 'db curl'
    DB_HAMMER = 'db hammer curl'
    CB_HAMMER = 'cable hammer curl'


class TricepMovements(EnumWithHelpers):
    DB_TRI_PRESS = 'db tri press'
    DB_TRI_EXT = 'db tri extension'
    CB_TRI_PULL = 'cable tri pulldown'


class ShoulderMovements(EnumWithHelpers):
    DB_LAT_RAISE = 'db lateral raise'
    DB_DELT_RAISE = 'db delt raise'
    DB_FRONT_RAISE = 'db front raise'
    DB_SHLD_PRESS = 'db shoulder press'
    CB_FACE_PULL = 'cable face pull'


class BackMovements(EnumWithHelpers):
    CB_LAT_PULL = 'cable lat pulldown'
    CB_ROW = 'cable row'
    DB_ROW = 'db row'
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


class CalfMovements(EnumWithHelpers):
    CALF_RAISE = 'calf raises'


# Custom error type because why not?
class PropertyTypeError(Exception):

    def __init__(
            self,
            given_property
    ):
        self.message = f'{given_property} is not of type \'key\' or \'value\''
