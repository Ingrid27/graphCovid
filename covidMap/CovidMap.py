import pycountry
import plotly.express as px
import chart_studio.plotly as py
import chart_studio
import plotly.graph_objs as go
import pandas as pd
import plotly.offline as pyoff

#chart_studio.tools.set_credentials_file(username='ingrid27', api_key='8IlQYVwLEREyvVY6xwA4')

url = ("https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv")
df = pd.read_csv(url)
df = df[["Date", "Country/Region",'Province/State', "Confirmed", "Recovered", "Deaths"]]

a = "Confirmed"
b = "Recovered"
c = "Deaths"

case = c

df1 = pd.DataFrame(df.groupby(["Country/Region","Date"]).sum()[case])

df1.to_csv('covid19.csv')

df1 = pd.read_csv('covid19.csv')

list_countries = df1['Country/Region'].unique().tolist()

d_country_code = {} 
for country in list_countries:
    try:
        country_data = pycountry.countries.search_fuzzy(country)
        country_code = country_data[0].alpha_3
        d_country_code.update({country: country_code})
    except:
        print('could not add ISO 3 code for ->', country)
        d_country_code.update({country: ' '})

for k, v in d_country_code.items():
    df1.loc[(df1['Country/Region'] == k), 'iso_alpha'] = v

fig = px.choropleth(data_frame = df1,
                    locations= "iso_alpha",
                    color= case,  # value in column 'Confirmed' determines color
                    hover_name= "Country/Region",
                    color_continuous_scale= ['#eae2b7', '#fcbf49', '#f77f00', '#F92B2B', '#A10505'],  #  color scale red, yellow green
                    animation_frame= "Date")

#py.iplot(fig, filename=case)

pyoff.plot(fig, filename='./covidMap/map'+case+'.html')
