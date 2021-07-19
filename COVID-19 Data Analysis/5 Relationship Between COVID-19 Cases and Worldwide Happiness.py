# reads CSV file, drops unrelated columns
happiness_report_csv = pd.read_csv('worldwide_happiness_report.csv')
happiness_report_csv.drop(['Overall rank', 'Score', 'Generosity', 'Perceptions of corruption'], axis=1, inplace=True)

# sets the index to be the Country or region, rather than a number
happiness_report_csv.set_index('Country or region', inplace=True)

# joins the COVID cases dataset with the world happiness report dataset
df = covid_data.join(happiness_report_csv, how='inner')

# graphically displays the correlation between COVID cases and characteristics of the most developed countries
df.corr()
