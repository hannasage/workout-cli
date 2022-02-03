
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

class Quad_Movements:
    SQUAT = 'squat'
    LUNGE_WALK = 'walking lunges'
    STEP_UPS = 'step ups'

    def get_all():
        return [
            Quad_Movements.SQUAT,
            Quad_Movements.LUNGE_WALK,
            Quad_Movements.STEP_UPS
        ]

class Ham_Movements:
    RDL = 'rdl'
    SL_RDL = 'single-leg rdl'

    def get_all():
        return [
            Ham_Movements.RDL,
            Ham_Movements.SL_RDL
        ]
 
class Calf_Movements:
    CALF_RAISE = 'calf raises'

    def get_all():
        return [
            Calf_Movements.CALF_RAISE
        ]