import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#reading git data
data = pd.read_csv("https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv")

print ('Primeiros 3 itens da lista:')
print (data.head(3))



"""

Confirmed cases:

"""

#classification of data by date and number of confirmed cases
cases = data.sort_values(['Date', 'Confirmed'], ascending=False).head(10)

print ("\nlista dos 10 países com maior número de casos confirmados pelo Covid-19:".upper())
print(cases)

countryCases = cases['Country/Region']
confirmed = cases['Confirmed']

plt.style.use("ggplot")
plt.figure(figsize=(20, 12))

plt.subplot(2, 2, 1)
plt.bar(countryCases, confirmed)
plt.title('10 países com o maior número de casos confirmados pelo Covid-19'.upper())
plt.ylabel('Número de Casos'.upper())
plt.xlabel('Países'.upper())


#classification of data by date and number of recovered cases

recovered = data.sort_values(['Date', 'Recovered'], ascending=False).head(10)

print ("\nlista dos 10 países com maior número de casos de recuperados do Covid-19:".upper())
print(recovered)

countryRecovered = recovered['Country/Region']
confirmedRecovered = recovered['Recovered']


plt.subplot(2, 2, 2)
plt.bar(countryRecovered, confirmedRecovered)
plt.title('10 países com o maior número de casos de recuperados do Covid-19'.upper())
plt.ylabel('Número de Casos'.upper())
plt.xlabel('Países'.upper())


#classification of data by date and number of deaths

deaths = data.sort_values(['Date', 'Deaths'], ascending = False).head(10)


print ("\nlista dos 10 países com maior número de casos de mortes pelo Covid-19:".upper())
print(deaths)

countryDeaths = deaths['Country/Region']
confirmedDeaths = deaths['Deaths']


plt.subplot(2, 2, 3)
plt.bar(countryDeaths, confirmedDeaths)
plt.title('10 países com maior número de casos de mortes pelo Covid-19'.upper())
plt.ylabel('Número de Mortes'.upper())
plt.xlabel('Países'.upper())

plt.savefig('confirmed.jpg')
plt.tight_layout()
plt.show()

