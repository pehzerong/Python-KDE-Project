import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.image as mpimg

df2011 = pd.read_excel (r'/Users/zerongpeh/Desktop/Project/2011.xlsx')
df2012 = pd.read_excel (r'/Users/zerongpeh/Desktop/Project/2012.xlsx')
df2013 = pd.read_excel (r'/Users/zerongpeh/Desktop/Project/2013.xlsx')
df2014 = pd.read_excel (r'/Users/zerongpeh/Desktop/Project/2014.xlsx')
df2015 = pd.read_excel (r'/Users/zerongpeh/Desktop/Project/2015.xlsx')
df2016 = pd.read_excel (r'/Users/zerongpeh/Desktop/Project/2016.xlsx')
df2017 = pd.read_excel (r'/Users/zerongpeh/Desktop/Project/2017.xlsx')
df2018 = pd.read_excel (r'/Users/zerongpeh/Desktop/Project/2018.xlsx')
df2019 = pd.read_excel (r'/Users/zerongpeh/Desktop/Project/2019.xlsx')
df2020 = pd.read_excel (r'/Users/zerongpeh/Desktop/Project/2020.xlsx')


npc_location = pd.read_excel (r'/Users/zerongpeh/Desktop/Project/npc_location.xlsx')



list_of_df = [df2011,df2012,df2013,df2014,df2015,df2016,df2017,df2018,df2019,df2020]
year = 2011

for df in list_of_df:
    df = df.pivot_table(index=['year','level_1'], columns='level_2', values ='value')
    df = df.reset_index()
    df['Total'] = df['Harassment'] + df['Unlicensed Moneylending']
    df = df.merge(npc_location,on=['level_1'])
    kde_graph = sns.kdeplot(x=df['x_axis'],y=df['y_axis'],weights=df['Total'],color='b',fill=True,alpha=0.85)
    kde_graph.set(xlim=(1.24001,1.48),ylim=(103.6,104.02994),aspect='auto')
    kde_graph.set(title=year)
    kde_graph.set(xlabel="Longitude")
    kde_graph.set(ylabel="Latitude")
    map_img = mpimg.imread(r'/Users/zerongpeh/Desktop/Project/Capture.PNG')
    final_graph= kde_graph.imshow(map_img,extent=[1.24001,1.48,103.6,104.02994],aspect='auto')
    final_graph = plt.savefig(r'/Users/zerongpeh/Desktop/Results/_' + str(year) + '.png', dpi=300)
    plt.show()
    year += 1

