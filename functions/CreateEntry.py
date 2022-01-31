import pandas as pd
from classes.Macros import Macros

def create_entry(file_path, clazz):
    # Read in and display current log tail and dtypes
    log = pd.read_csv(file_path, index_col=0)
    print(log.tail(10))
    print(log.dtypes)

    # Collect new workout information
    new_entry = clazz.create(clazz)

    # Convert workout into dataframe
    entry_as_df = pd.DataFrame(clazz.to_dict(new_entry))
    print(entry_as_df)

    # Add new entry to workout_log
    updated_log = pd.concat([log, entry_as_df]).reset_index(drop=True)

    # Show new dataframe tail and confirm export 
    print(updated_log.tail(10))

    save = input('Overwrite old copy with new data? [y/n]: ')
    if save == 'y' or save == 'Y':
        updated_log.to_csv(file_path)
    else:
        print('File not saved, goodbye!')