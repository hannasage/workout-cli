import click
from apps.WorkoutApp import *
from apps.NutritionApp import *

macro_log = 'C:/Projects/workout-cli/data/macros-log.csv'
workout_log = 'C:/Projects/workout-cli/data/workout-log.csv'


@click.command()
@click.option('--app', default='all', help='Applications include: workout, nutrition')
def main(app):
    runner(app)


def farewell():
    print('Shutting down, goodnight!')


def runner(app_index):
    if app_index == WorkoutApp.callsign():
        WorkoutApp().create_entry()
    elif app_index == NutritionApp.callsign():
        NutritionApp().create_entry()
    elif app_index == 'all':
        App().create_entry()
        WorkoutApp().create_entry()
        NutritionApp().create_entry()
    else:
        farewell()


if __name__ == '__main__':
    main()
