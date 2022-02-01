
class Macros:

    def __init__(self,
                 protein,
                 carbs,
                 fats,
                 cals) -> None:
        self.protein = protein
        self.carbs = carbs
        self.fats = fats
        self.cals = cals

    # Enumerate class callsign
    def callsign():
        return 'macros'

    # Converts to an item that pandas will turn into a DataFrame
    def to_dict(self):
        return {
            'protein': [self.protein],
            'carbs': [self.carbs],
            'fats': [self.fats],
            'calories': [self.cals]
        }
    
    # Prompts the user for the column name passed in
    def prompt(column_header):
        return input(f'Enter {column_header}: ')
    
    # Aggregates all the prompts into a single method call
    def create(self):
        protein = self.prompt('protein')
        carbs = self.prompt('carbs')
        fats = self.prompt('fats')
        cals = self.prompt('calories')
        return Macros(protein,
                      carbs,
                      fats,
                      cals)