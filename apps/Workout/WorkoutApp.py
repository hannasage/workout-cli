from apps.Workout.classes.Workout import Workout
import pandas as pd

class WorkoutApp:

    def __init__(self) -> None:
        self.path = 'C:\Projects\workout-cli\data\workout-log.csv'
    
    def create_entry(self):
        # Read in and display current log tail and dtypes
        log = pd.read_csv(self.path, index_col=0)
        print(log.tail(10))
        print(log.dtypes)

        # Collect new workout information
        new_entry = Workout.builder()

        # Convert workout into dataframe
        entry_as_df = pd.DataFrame(Workout.to_dict(new_entry))
        print(entry_as_df)

        # Add new entry to workout_log
        updated_log = pd.concat([log, entry_as_df]).reset_index(drop=True)

        # Show new dataframe tail and confirm export 
        print(updated_log.tail(10))

        save = input('Overwrite old copy with new data? [y/n]: ')
        if save == 'y' or save == 'Y':
            updated_log.to_csv(self.path)
        else:
            print('File not saved, goodbye!')
        