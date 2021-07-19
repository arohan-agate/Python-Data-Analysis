countries = list(df_covid.index)
max_infection_rates = []
for c in countries:
    max_infection_rates.append(df_covid.loc[c].diff().max())
df_covid['max infection rate'] = max_infection_rates

covid_data = pd.DataFrame(df_covid['max infection rate'])
display(covid_data)
