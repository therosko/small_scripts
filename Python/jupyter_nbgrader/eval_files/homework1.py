import pandas as pd

def import_dataset(x):
    import pandas as pd
    path_to_file = "data/" + str(x) + ".csv"
    data = pd.read_csv(path_to_file)
    return data