from apps.classes.App import App
from classes.Movement import to_dict_from_list
from classes.Workout import Workout

import pandas as pd


class WorkoutApp(App):

    def __init__(self) -> None:
        self.workout_log_path = 'C:/Projects/workout-cli/data/workouts-log.csv'
        self.movements_log_path = 'C:/Projects/workout-cli/data/movements-log.csv'
        self.volumes_log_path = 'C:/Projects/workout-cli/data//volumes-log.csv'

    def create_entry(self):
        # Read in and display current log tail and dtypes
        workouts_log = pd.read_csv(self.workout_log_path, index_col=0)
        movements_log = pd.read_csv(self.movements_log_path, index_col=0)
        volumes_log = pd.read_csv(self.volumes_log_path, index_col=0)

        # View latest 10 entries
        print(workouts_log.tail(10))
        print(movements_log.tail(10))
        print(volumes_log.tail(10))

        # View dtypes
        # print(workouts_log.dtypes)
        # print(movements_log.dtypes)
        # print(volumes_log.dtypes)

        # Collect new workout information
        movement_count = int(input('How many movements did you do?: '))
        workout_entry: Workout = Workout.builder(movement_count)

        # Convert workout into dataframes
        workout_df = pd.DataFrame(workout_entry.to_dict())
        movements_df = pd.DataFrame(to_dict_from_list(workout_entry.movements))
        volumes_df = pd.DataFrame(workout_entry.volumes.to_dict())

        # Add new entry to workout_log
        updated_workouts_log = pd.concat([workouts_log, workout_df]).reset_index(drop=True)
        updates_movements_log = pd.concat([movements_log, movements_df]).reset_index(drop=True)
        updated_volumes_log = pd.concat([volumes_log, volumes_df]).reset_index(drop=True)

        # Show new dataframe tail and confirm export 
        print("\n========== WORKOUTS ==========")
        print(updated_workouts_log.tail(10))
        print("\n========== MOVEMENTS ==========")
        print(updates_movements_log.tail(10))
        print("\n========== VOLUMES ==========")
        print(updated_volumes_log.tail(10))

        save = input('Write new data? [y/n]: ')
        if save == 'y' or save == 'Y':
            updated_workouts_log.to_csv(self.workout_log_path)
            updates_movements_log.to_csv(self.movements_log_path)
            updated_volumes_log.to_csv(self.volumes_log_path)
        else:
            print('Data not saved, goodbye!')
            self.quit()
