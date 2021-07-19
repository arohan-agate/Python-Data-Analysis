# Create random weights for the stocks and normalize them
weights = np.array(np.random.random(3))

# Ensure that the sum of all weights are = 1
weights = weights / np.sum(weights)
print(weights)

# Normalize the stock values 
df_portfolio = normalize(stocks_df)
display(df_portfolio)

# Creates a DF in which the portfolio value starts at $1M with random distributions
for counter, stock in enumerate(df_portfolio.columns[1:]):
  df_portfolio[stock] = df_portfolio[stock] * weights[counter]
  df_portfolio[stock] = df_portfolio[stock] * 1000000
display(df_portfolio)

# Creates an additional column that contains the sum of all stock values in the portfolio
df_portfolio['portfolio daily worth in $'] = df_portfolio[df_portfolio != 'Date'].sum(axis = 1)
display(df_portfolio)
