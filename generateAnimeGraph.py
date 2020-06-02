import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
from matplotlib import animation as anime
from IPython.display import HTML


#reading git data
#data = pd.read_csv("../covid-19/data/time-series-19-covid-combined.csv")
data = pd.read_csv("https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv")

#Dataset with the columns we are using right now
data.head(5)
data = data[["Date", "Country/Region", "Confirmed", "Recovered", "Deaths"]]


#colors            0          1         2          3           4         5          6          7          8          9
colorOne =   ['#D62828', '#362736', '#F77F00', '#6B2C39', '#FCBF49', '#002132', '#3A5C6A', '#E25850', '#1CA3D1', '#581503']
colorTwo =   ['#43AA8B', '#F3722C', '#204525', '#F9C74F', '#F94144', '#90BE6D', '#F65A38', '#577590', '#F8961E', '#C5C35E']
colorThree = ['#000000', '#53B3CB', '#7FB800', '#AD352A', '#00A6ED', '#3C1804', '#F9C22E', '#0D2C54', '#E01A4F', '#545255']


fig, ax = plt.subplots(figsize=(15, 20))
#confirmed cases method
def confirmedBarChart(date, case = "Confirmed"):
    # classification of data by date and number of confirmed cases
    # grouping the count of cases in the countries by date
    casesIn = data.groupby(['Country/Region', 'Date'])
    covidConfirmed = casesIn.sum().reset_index().sort_values(['Date'], ascending=False)

    # New dataframe for make the animation
    dfConfirmed = (
        covidConfirmed[covidConfirmed['Date'].eq(date)].sort_values(by="Confirmed", ascending=False).head(10))
    dfConfirmed.tail(10)

    # Last date
    dateAt = dfConfirmed.iloc[2][1]

    print('\nUltima atualização: {}'.format(dateAt).upper())

    print("\nlista dos 10 países com maior número de casos confirmados pelo Covid-19:".upper())
    print(dfConfirmed.tail(10))

    # aux for the graph
    countryCases = dfConfirmed['Country/Region']
    confirmed = dfConfirmed['Confirmed']

    # plotting config
    plt.style.use("ggplot")


    # print the numburs on the bar graph
    for i, v in enumerate(confirmed):
        ax.text(v, i, " " + str(v), va='center', fontweight='bold')


    ax.barh(countryCases, confirmed, color=colorOne)
    ax.set_title('\n10 países com o maior número de casos confirmados pelo Covid-19')
    ax.text(0, 1.06, 'Número de Casos\nÚltima atualização: {}\n'.format(dateAt).upper(), size=12)
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', labelsize=12)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    # ax.ylabel('Países\n')
    ax.invert_yaxis()  # labels read top-to-bottom
    plt.box(False)

confirmedBarChart("2020-04-17")
# animation
animator = anime.FuncAnimation(fig, confirmedBarChart, frames=data.Date.unique(), interval=300, repeat=False)
HTML(animator.to_jshtml())
animator.save("casosCovi-19.html")