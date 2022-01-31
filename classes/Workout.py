
class Workout: 
    
    def __init__(self, 
                date,
                duration, 
                cals, 
                split, 
                total_vol, 
                ch_vol, 
                bi_vol,
                tri_vol, 
                shld_vol,
                bk_vol, 
                core_vol, 
                qd_vol, 
                ham_vol, 
                cf_vol) -> None:
        self.date = date
        self.duration = duration
        self.cals = cals
        self.split = split
        self.total_vol = total_vol
        self.ch_vol = ch_vol
        self.bi_vol = bi_vol
        self.tri_vol = tri_vol
        self.shld_vol = shld_vol
        self.bk_vol = bk_vol
        self.core_vol = core_vol
        self.qd_vol = qd_vol
        self.ham_vol = ham_vol
        self.cf_vol = cf_vol

    # Enumerate class callsign
    def callsign():
        return 'workout'

    # Converts to an item that pandas will turn into a DataFrame
    def to_dict(self):
        return {
            'date': [self.date],
            'duration': [self.duration],
            'calse': [self.cals],
            'split': [self.split],
            'total_vol': [self.total_vol],
            'ch_vol': [self.ch_vol],
            'bi_vol': [self.bi_vol],
            'tri_vol': [self.tri_vol],
            'shld_vol': [self.shld_vol],
            'back_vol': [self.bk_vol],
            'core_vol': [self.core_vol],
            'quad_vol': [self.qd_vol],
            'ham_vol': [self.ham_vol],
            'cf_vol': [self.cf_vol]
        }
    
    # Prompts the user for the column name passed in
    def prompt(column_header):
        return input(f'Enter {column_header}: ')
    
    # Aggregates all the prompts into a single method call
    def create(self):
        date = self.prompt('date')
        duration = self.prompt('duration')
        cals = self.prompt('total cals')
        split = self.prompt('split')
        total_vol = self.prompt('total volume')
        ch_vol = self.prompt('chest volume')
        bi_vol = self.prompt('bicep volume')
        tri_vol = self.prompt('tricep volume')
        shld_vol = self.prompt('shoulder volume')
        bk_vol = self.prompt('back volume')
        core_vol = self.prompt('core volume')
        qd_vol = self.prompt('quad volume')
        ham_vol = self.prompt('hamstring volume')
        cf_vol = self.prompt('calf volume')
        return Workout(date,
                        duration,
                        cals,
                        split,
                        total_vol,
                        ch_vol,
                        bi_vol,
                        tri_vol,
                        shld_vol,
                        bk_vol,
                        core_vol,
                        qd_vol,
                        ham_vol,
                        cf_vol)
