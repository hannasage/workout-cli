from apps.classes.App import App
from apps.classes.Nutrition import Nutrition
import pandas as pd

class NutritionApp(App):

    def __init__(self) -> None:
        self.nutrition_log_path = 'C:\Projects\workout-cli\data\\nutrition-log.csv'
        self.workout_log_path = 'C:\Projects\workout-cli\data\workouts-log.csv'

    def create_entry(self):
        # Read in and display current log tail and dtypes
        log = pd.read_csv(self.nutrition_log_path, index_col=0)
        workout_log = pd.read_csv(self.workout_log_path, index_col=0)

        # Get workout relation
        workout_id = check_workout_relation(workout_log)

        # Collect new nutrition information
        new_entry = Nutrition.create(workout_id)

        # Convert Nutrition object into dataframe
        entry_as_df = pd.DataFrame(Nutrition.to_dict(new_entry))
        print(entry_as_df)

        # Add new entry to nutrition_log
        updated_log = pd.concat([log, entry_as_df]).reset_index(drop=True)

        # Show new dataframe tail and confirm export 
        print(updated_log.tail(10))

        save = input('Overwrite old copy with new data? [y/n]: ')
        if save == 'y' or save == 'Y':
            updated_log.to_csv(self.nutrition_log_path)
        else:
            self.quit()


def check_workout_relation(log: pd.DataFrame):
    print(log.tail())
    workout_index = None
    try:
        workout_index = int(input('Which workout (by index) should we link it to? (RETURN to cont.): '))
        return log.iloc[workout_index].id
    except:
        relation = input('Is this related to a workout? [y/n]: ')
        if relation.lower() == 'y':
            check_workout_relation(log)
        else:
            pass

    return None
        