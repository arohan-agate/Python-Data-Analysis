# Plot the portfolio daily return
fig = px.line(x = df_portfolio.Date, y = df_portfolio['portfolio daily % return'], title = 'Sample Portfolio Daily % Return')
fig.show()

# Plot all stocks (normalized)
i_plot(df_portfolio.drop(['portfolio daily worth in $', 'portfolio daily % return'], axis = 1), 'Sample Portfolio Individual Stocks Value ($) ')

# Print out a histogram of daily returns
fig = px.histogram(df_portfolio, x = 'Sample portfolio daily % return')
fig.show()

fig = px.line(x = df_portfolio.Date, y = df_portfolio['portfolio daily worth in $'], title = 'Sample Portfolio Daily Worth ($)')
fig.show()
