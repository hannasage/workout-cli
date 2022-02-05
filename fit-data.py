import click
from apps.Workout.WorkoutApp import *
from apps.Macros.MacrosApp import *
from apps.Macros.classes.Macros import Macros
from apps.Workout.classes.Workout import Workout

macro_log = 'C:\Projects\workout-cli\data\macros-log.csv'
workout_log = 'C:\Projects\workout-cli\data\workout-log.csv'

@click.command()
@click.option('--app', default='workout', help='Create and save a workout log entry')
def main(app):
    runner(app)


def farewell():
    print('Shutting down, goodnight!')


def runner(app_index):
    if app_index == Workout.callsign():
        WorkoutApp().create_entry()
    elif app_index == Macros.callsign():
        MacrosApp().create_entry()
    else:
        farewell()


if __name__ == '__main__':
    main()
