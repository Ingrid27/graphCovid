
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import matplotlib
import matplotlib.ticker as ticker
from datetime import date
from matplotlib import animation as anime
from IPython.display import display, clear_output, HTML, Image


#download and save csv file from github
url = ("https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv")
req = requests.get(url)
url_content = req.content
csv_file = open('covidAnimation/covid19.csv', 'wb')
csv_file.write(url_content)
csv_file.close()

#reading data
covid = pd.read_csv('covidAnimation/covid19.csv')
covid = covid[["Date", "Country/Region", "Confirmed", "Recovered", "Deaths"]]

# grouping the count of cases in the countries by date
casesIn = covid.groupby(['Country/Region', 'Date'])
covidConfirmed = casesIn.sum().reset_index().sort_values(['Date'], ascending=False)

# Last date
dateAt = covid.iloc[-1][0]

#colors            0          1         2          3           4         5          6          7          8          9
colorOne =   ['#D62828', '#362736', '#F77F00', '#6B2C39', '#FCBF49', '#002132', '#3A5C6A', '#E25850', '#1CA3D1', '#581503']
colorTwo =   ['#43AA8B', '#F3722C', '#204525', '#F9C74F', '#F94144', '#90BE6D', '#F65A38', '#577590', '#F8961E', '#C5C35E']
colorThree = ['#000000', '#53B3CB', '#7FB800', '#AD352A', '#00A6ED', '#3C1804', '#F9C22E', '#0D2C54', '#E01A4F', '#545255']

# plotting config
plt.style.use("ggplot")
fig, ax =  plt.subplots(figsize = (20, 12))

#confirmed cases method
def confirmedBarChart(dateTime, case = "Confirmed"):
    # New dataframe for make the animation
    dfConfirmed = (
        covidConfirmed[covidConfirmed['Date'].eq(dateTime)].sort_values(by=case, ascending=False).head(10))
    dfConfirmed.tail(10)
    ax.clear()

    #date Update
    dateNow = dfConfirmed.iloc[2][1]

    print('\nUltima atualização: {}'.format(dateNow).upper())
    print("\nlista dos 10 países com maior número de casos confirmados pelo Covid-19:".upper())
    print(dfConfirmed.tail(10))

    # aux for the graph
    countryCases = dfConfirmed['Country/Region']
    confirmed = dfConfirmed['Confirmed']

    plt.style.use("ggplot")
    ax.set_title('\n10 países com o maior número de casos confirmados pelo Covid-19')
    dx = dfConfirmed[case].max() / 200

    for i, v in enumerate(confirmed):
        ax.text(v-dx, i, " " + str(v), size = 14, ha = 'left', va='center', fontweight='bold')

    ax.barh(countryCases, confirmed, color=colorOne)
    ax.invert_yaxis() 
    ax.text(0.5, -0.1, 'Número de Casos\nÚltima atualização: {}\n'.format(dateAt).upper(), ha = 'center', va = 'center', transform=ax.transAxes, size=14)
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('bottom')
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(1, 0.4, dateNow, transform=ax.transAxes, size=36, ha='right', color = '#3A5C6A')
    # plt.box(True)
    
    # plt.savefig("graph2.png")
    print("DATA DA ÚLTIMA ATUALIZAÇÃO DE DADOS: {}".format(dateAt))



confirmedBarChart(dateAt)

animator = anime.FuncAnimation(fig,confirmedBarChart,frames=covid.Date.unique(), interval=400, blit=False, repeat=False)
animator.save('covidAnimation/cases_video.mp4')
plt.show()