import click
from apps.Nutrition.NutritionApp import NutritionApp
from apps.Workout.WorkoutApp import *
from apps.Nutrition.NutritionApp import *
from apps.Workout.classes.Workout import Workout

macro_log = 'C:\Projects\workout-cli\data\macros-log.csv'
workout_log = 'C:\Projects\workout-cli\data\workout-log.csv'

@click.command()
@click.option('--app', default='nutrition', help='Applications include: workout, nutrition')
def main(app):
    runner(app)


def farewell():
    print('Shutting down, goodnight!')


def runner(app_index):
    if app_index == Workout.callsign():
        WorkoutApp().create_entry()
    elif app_index == Nutrition.callsign():
        NutritionApp().create_entry()
    else:
        farewell()


if __name__ == '__main__':
    main()
