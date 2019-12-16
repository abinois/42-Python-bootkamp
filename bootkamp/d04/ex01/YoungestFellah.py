
import pandas as pd
from FileLoader import FileLoader

def YoungestFellah(df, year):
    if type(df) is not pd.DataFrame or type(year) is not int or year < 1:
        exit('Wrong parameters.')
    sub_data = df[df.Year == year].sort_values('Age')
    if sub_data.empty is True:
        exit('Not an Olympic year.')
    dudes = sub_data[sub_data.Sex == 'M']
    chicks = sub_data[sub_data.Sex == 'F']
    dic = {
        dudes.loc[dudes.index[0]].Sex: dudes.Age.min(),
        chicks.loc[chicks.index[0]].Sex: chicks.Age.min() }
    return dic

if __name__ == '__main__':
    fl = FileLoader()
    dataframe = fl.load('../ex00/athlete_events.csv')
    print(YoungestFellah(dataframe, 2004))
    print(YoungestFellah(dataframe, 2003))

