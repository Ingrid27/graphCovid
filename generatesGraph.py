import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date


#reading git data
#data = pd.read_csv("../covid-19/data/time-series-19-covid-combined.csv")
data = pd.read_csv("https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv")



#colors            0          1         2          3           4         5          6          7          8          9
colorOne =   ['#D62828', '#362736', '#F77F00', '#6B2C39', '#FCBF49', '#002132', '#3A5C6A', '#E25850', '#1CA3D1', '#581503']
colorTwo =   ['#43AA8B', '#F3722C', '#204525', '#F9C74F', '#F94144', '#90BE6D', '#F65A38', '#577590', '#F8961E', '#C5C35E']
colorThree = ['#000000', '#53B3CB', '#7FB800', '#AD352A', '#00A6ED', '#3C1804', '#F9C22E', '#0D2C54', '#E01A4F', '#545255']


print ('Primeiros 3 itens da lista:')
print (data.head(3))



"""

Confirmed cases:

"""

#classification of data by date and number of confirmed cases
casesIn = data.sort_values(['Date', 'Confirmed'], ascending=False).head(10)
cases = casesIn.sort_values(['Date', 'Confirmed']).tail(10)

#Last date
dateAt=casesIn.head(1).iloc[0][0]

print('\nUltima atualização: {}'.format(dateAt).upper())

print ("\nlista dos 10 países com maior número de casos confirmados pelo Covid-19:".upper())
print(casesIn)

countryCases = cases['Country/Region']
confirmed = cases['Confirmed']



plt.style.use("ggplot")
plt.figure(figsize=(20, 15))

plt.subplot(2, 2, 1)
plt.barh(countryCases, confirmed, color=colorOne)
plt.title('\n10 países com o maior número de casos confirmados pelo Covid-19'.upper())
plt.xlabel('Número de Casos\nUltima atualização: {}\n'.format(dateAt).upper(), fontSize = 12)
plt.ylabel('Países\n'.upper())


for i, v in enumerate(confirmed):
    plt.text(v, i, " "+str(v), va='center', fontweight='bold')


#classification of data by date and number of recovered cases

recoveredIn = data.sort_values(['Date', 'Recovered'], ascending=False).head(10)
recovered = recoveredIn.sort_values(['Date', 'Recovered']).tail(10)

print ("\nlista dos 10 países com maior número de casos de recuperados do Covid-19:".upper())
print(recoveredIn)

countryRecovered = recovered['Country/Region']
confirmedRecovered = recovered['Recovered']


plt.subplot(2, 2, 2)
plt.barh(countryRecovered, confirmedRecovered, color=colorTwo)
plt.title('\n10 países com o maior número de casos de recuperados do Covid-19'.upper())
plt.xlabel('Número de Casos\nUltima atualização: {}'.format(dateAt).upper())
plt.ylabel('Países\n'.upper())


for i, v in enumerate(confirmedRecovered):
    plt.text(v, i, " "+str(v), va='center', fontweight='bold')


#classification of data by date and number of deaths

deathsIn = data.sort_values(['Date', 'Deaths'], ascending=False).head(10)
deaths = deathsIn.sort_values(['Date', 'Deaths']).tail(10)


print ("\nlista dos 10 países com maior número de casos de mortes pelo Covid-19:".upper())
print(deathsIn)

countryDeaths = deaths['Country/Region']
confirmedDeaths = deaths['Deaths']


plt.subplot(2, 2, 3)
plt.barh(countryDeaths, confirmedDeaths, color=colorThree)
plt.title('\n10 países com maior número de casos de mortes pelo Covid-19'.upper())
plt.xlabel('Número de Mortes\nUltima atualização: {}'.format(dateAt).upper())
plt.ylabel('Países\n'.upper())


for i, v in enumerate(confirmedDeaths):
    plt.text(v, i, " "+str(v), va='center', fontweight='bold')


plt.savefig('graph.jpg')
plt.tight_layout()
plt.show()
