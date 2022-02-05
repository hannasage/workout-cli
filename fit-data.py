import click
from apps.WorkoutApp import *
from apps.NutritionApp import *
from apps.classes.Workout import Workout
from apps.classes.Nutrition import Nutrition

macro_log = 'C:\Projects\workout-cli\data\macros-log.csv'
workout_log = 'C:\Projects\workout-cli\data\workout-log.csv'

@click.command()
@click.option('--app', default='all', help='Applications include: workout, nutrition')
def main(app):
    runner(app)


def farewell():
    print('Shutting down, goodnight!')


def runner(app_index):
    if app_index == Workout.callsign():
        WorkoutApp().create_entry()
    elif app_index == Nutrition.callsign():
        NutritionApp().create_entry()
    elif app_index == 'all':
        WorkoutApp().create_entry()
        NutritionApp().create_entry()
    else:
        farewell()


if __name__ == '__main__':
    main()
