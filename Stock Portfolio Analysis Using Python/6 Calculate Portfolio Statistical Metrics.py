display(df_portfolio)

# Cummulative return of the portfolio
cummulative_return = ((df_portfolio['portfolio daily worth in $'][-1:] - df_portfolio['portfolio daily worth in $'][0])/ df_portfolio['portfolio daily worth in $'][0]) * 100
print('Cummulative return of the portfolio is {} %'.format(cummulative_return.values[0]))

# Calculate the portfolio standard deviation
print('Standard deviation of portfolio = {}'.format(df_portfolio['portfolio daily % return'].std()))

# Calculate the average daily return 
print('Average daily return of portfolio = {}'.format(df_portfolio['portfolio daily % return'].mean()))

# Calculate the Sharpe Ratio
sharpe_ratio = df_portfolio['portfolio daily % return'].mean() / df_portfolio['portfolio daily % return'].std() * np.sqrt(252)
print('Sharpe ratio of the portfolio is {}'.format(sharpe_ratio))
