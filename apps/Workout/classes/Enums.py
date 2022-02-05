
class Volume_Enums:
    CHEST = 'chest'
    BICEP = 'bicep'
    TRICEP = 'tricep'
    SHOULDER = 'shoulder'
    BACK = 'back'
    CORE = 'core'
    QUADS = 'quads'
    HAMSTRINGS = 'hamstrings'
    CALF = 'calf'

    def get_all():
        return [
            Volume_Enums.CHEST,
            Volume_Enums.BICEP,
            Volume_Enums.TRICEP,
            Volume_Enums.SHOULDER,
            Volume_Enums.BACK,
            Volume_Enums.CORE,
            Volume_Enums.QUADS, 
            Volume_Enums.HAMSTRINGS,
            Volume_Enums.CALF
        ]

class Chest_Movements:
    DB_PRESS = 'db chest press'
    DB_FLY = 'db fly'
    DB_PRESS_INCL = 'incline db chest press'

    def get_all():
        return [
            Chest_Movements.DB_FLY,
            Chest_Movements.DB_PRESS,
            Chest_Movements.DB_PRESS_INCL
        ]

class Bicep_Movements:
    CHIN_UP = 'chin up'
    DB_CURL = 'db curl'
    DB_HAMMER = 'db hammer curl'
    CB_HAMMER = 'cable hammer curl'

    def get_all():
        return [
            Bicep_Movements.CHIN_UP,
            Bicep_Movements.DB_CURL,
            Bicep_Movements.DB_HAMMER,
            Bicep_Movements.CB_HAMMER
        ] 

class Tricep_Movements:
    DB_TRI_PRESS = 'db tri press'
    DB_TRI_EXT = 'db tri extension'
    CB_TRI_PULL = 'cable tri pulldown'

    def get_all():
        return [
            Tricep_Movements.DB_TRI_EXT,
            Tricep_Movements.DB_TRI_PRESS,
            Tricep_Movements.CB_TRI_PULL
        ] 

class Shoulder_Movements:
    DB_LAT_RAISE = 'db lateral raise'
    DB_DELT_RAISE = 'db delt raise'
    DB_FRONT_RAISE = 'db front raise'
    DB_SHLD_PRESS = 'db shoulder press'
    CB_FACE_PULL = 'cable face pull'

    def get_all():
        return [
            Shoulder_Movements.DB_DELT_RAISE,
            Shoulder_Movements.DB_FRONT_RAISE,
            Shoulder_Movements.DB_SHLD_PRESS,
            Shoulder_Movements.DB_LAT_RAISE,
            Shoulder_Movements.CB_FACE_PULL
        ] 

class Back_Movements:
    CB_LAT_PULL = 'cable lat pulldown'
    CB_ROW = 'cable row'
    DB_ROW = 'db row'
    PULL_UP = 'pull up'

    def get_all():
        return [
            Back_Movements.CB_LAT_PULL,
            Back_Movements.CB_ROW,
            Back_Movements.DB_ROW,
            Back_Movements.PULL_UP
        ] 

class Core_Movements:
    CRUNCH = 'crunches'
    CB_AXES = 'cable axes'

    def get_all():
        return [
            Core_Movements.CRUNCH,
            Core_Movements.CB_AXES
        ]

class Quad_Movements:
    SQUAT = 'squat'
    LUNGE = 'lunges'
    LUNGE_WALK = 'walking lunges'
    STEP_UPS = 'step ups'

    def get_all():
        return [
            Quad_Movements.SQUAT,
            Quad_Movements.LUNGE,
            Quad_Movements.LUNGE_WALK,
            Quad_Movements.STEP_UPS
        ] 

class Ham_Movements:
    RDL = 'rdl'
    SL_RDL = 'single-leg rdl'
    CB_PULL_THRU = 'cable pull through'

    def get_all():
        return [
            Ham_Movements.RDL,
            Ham_Movements.SL_RDL,
            Ham_Movements.CB_PULL_THRU
        ] 
 
class Calf_Movements:
    CALF_RAISE = 'calf raises'

    def get_all():
        return [
            Calf_Movements.CALF_RAISE
        ] 