# displays the number of confirmed cases every day over a 3 month period
df_covid.loc['China'].plot()
df_covid.loc['Italy'].plot()
df_covid.loc['US'].plot()
df_covid.loc['India'].plot()
df_covid.loc['Australia'].plot()
df_covid.loc['Brazil'].plot()
df_covid.loc['Kenya'].plot()
plt.legend()
