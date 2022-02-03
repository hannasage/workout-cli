from apps.Workout.classes.Movement import Movement, to_dict_from_list
from apps.Workout.classes.Workout import Workout
import pandas as pd

class WorkoutApp:

    def __init__(self) -> None:
        self.movements_log_path = 'C:\Projects\workout-cli\data\movements-log.csv'
        self.volumes_log_path = 'C:\Projects\workout-cli\data\volumes-log.csv'
    
    def create_entry(self):
        # Read in and display current log tail and dtypes
        movements_log = pd.read_csv(self.movements_log_path, index_col=0)
        volumes_log = pd.read_csv(self.volumes_log_path, index_col=0)

        # View latest 10 entries
        print(movements_log.tail(10))
        print(volumes_log.tail(10))

        # View dtypes
        print(movements_log.dtypes)
        print(volumes_log.dtypes)

        movement_count = int(input('How many movements did you do?: '))
        # Collect new workout information
        workout_entry: Workout = Workout.builder(movement_count)

        # Convert workout into dataframes
        movements_df = pd.DataFrame(to_dict_from_list(workout_entry.movements))
        volumes_df = pd.DataFrame(workout_entry.volumes.to_dict())
        print(movements_df)
        print(volumes_df)

        # Add new entry to workout_log
        updates_movements_log = pd.concat([movements_log, movements_df].reset_index(drop=True))
        updated_volumes_log = pd.concat([volumes_log, volumes_df]).reset_index(drop=True)

        # Show new dataframe tail and confirm export 
        print(updates_movements_log.tail(10))
        print(updated_volumes_log.tail(10))

        save = input('Overwrite old copy with new data? [y/n]: ')
        if save == 'y' or save == 'Y':
            updated_volumes_log.to_csv(self.volumes_log_path)
        else:
            print('File not saved, goodbye!')
        