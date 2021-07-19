covid_dataset_csv = pd.read_csv('covid19_Confirmed_dataset.csv')
covid_dataset_csv.drop(['Lat', 'Long'], axis = 1, inplace=True)
df_covid = covid_dataset_csv.groupby('Country/Region').sum()
display(df_covid)
