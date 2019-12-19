from matplotlib import pyplot, rcParams as rcp

class MyPlotLib():
    def __init__(self):
        rcp['figure.facecolor'] = 'yellow' # background color
        rcp['axes.edgecolor'] = 'royalblue' # change all 4 axes color
        rcp['axes.linewidth'] = 2.5
        rcp['axes.grid'] = True #display grid
        rcp['grid.color'] = 'lightgreen'
        
    def histogram(self, data, features):
        for f in features:
            pyplot.title(f, {'fontname':'Arial black', 'color':'royalblue', 'fontsize':17.0, 'verticalalignment':'bottom'})
            histo = pyplot.hist(data[f], color='pink')
            pyplot.show(histo)

    def density(self, data, features):
        rcp['axes.labelcolor'] = 'royalblue'
        rcp['axes.labelsize'] = 15.0
        pyplot.show(data[features].plot.kde(bw_method=0.1))

    def pair_plot(self, data, features):
        pass

    def box_plot(self, data, features):
        print('hahaha')
        data = data.dropna()
        liste = []
        for f in features:
            liste.append(data[f])
        _, ax = pyplot.subplots()
        ax.boxplot(liste)
        pyplot.show()



if __name__ == '__main__':

    from FileLoader import FileLoader
    fl = FileLoader()
    dataframe = fl.load('../ex00/athlete_events.csv')
    plot = MyPlotLib()
    # plot.histogram(dataframe, ['Weight', 'Height'])
    # plot.density(dataframe, ['Weight', 'Height'])
    # plot.box_plot(dataframe, ['Weight', 'Height'])
    plot.pair_plot(dataframe, ['Weight', 'Height'])
