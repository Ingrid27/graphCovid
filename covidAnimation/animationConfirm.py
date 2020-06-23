
import pandas as pd
import bar_chart_race as bcr
import requests

#download and save csv file from github
url = ("https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv")
req = requests.get(url)
url_content = req.content
csv_file = open('covidAnimation/covid19.csv', 'wb')
csv_file.write(url_content)
csv_file.close()

#reading data
covid = pd.read_csv("covidAnimation/covid19.csv")
covid = covid[["Date", "Country/Region", "Confirmed", "Recovered", "Deaths"]]

a = "Confirmed"
b = "Recovered"
c = "Deaths"

case = b

dfCovidBcr = pd.DataFrame(covid.groupby(["Country/Region","Date"]).sum()[case]).unstack().T.droplevel(level=0)

bcr.bar_chart_race(dfCovidBcr, 
                    './covidAnimation/'+case+'_video.mp4',
                    bar_label_size=10, 
                    tick_label_size=10,
                    n_bars=10, 
                    filter_column_colors = True,
                    cmap= 'dark24',
                    period_label={'x': .99, 'y': .1, 'ha': 'right', 'color': 'black', 'size': 20},
                    #title="10 países com o maior número de casos de recuperados do Covid-19".upper(), 
                    #steps_per_period=10,
                    period_length=900,
                    #figsize=(10, 3), =====> a
                    figsize=(7, 5),
                    dpi=100
                    )