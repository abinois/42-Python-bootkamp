from FileLoader import FileLoader

def howManyMedals(df, name):
    sub_data = df[df.Name == name]
    if sub_data.empty:
        exit('Inconnu au bataillzer.')
    print(sub_data.groupby('Medal').count())
    return sub_data

if __name__ == '__main__':
    fl = FileLoader()
    dataframe = fl.load('../ex00/athlete_events.csv')
    print(howManyMedals(dataframe, 'Kjetil Andr Aamodt'))