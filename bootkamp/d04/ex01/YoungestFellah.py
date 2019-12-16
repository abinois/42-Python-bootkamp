
import pandas as pd
from FileLoader import FileLoader

def YoungestFellah(df, year):
    sub_data = df[df.Year == year]
    dudes = sub_data[sub_data.Sex == 'M']
    chicks = sub_data[sub_data.Sex == 'F']
    dic = {
        'M':dudes.Age.min(),
        'F':chicks.Age.min()
    }
    return dic

if __name__ == '__main__':
    fl = FileLoader()
    dataframe = fl.load('../ex00/athlete_events.csv')
    print(YoungestFellah(dataframe, 2004))
