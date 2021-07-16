portfolio_dtf = pd.DataFrame({'ticker symbol':['AAPL', 'AMZN', 'GME'],
                               'num shares':[12, 3, 30],
                                'price per share':[150, 3630, 165]})
portfolio_dtf

stock_dollar_value = portfolio_dtf['num shares'] * portfolio_dtf['price per share']
stock_dollar_value

stock_dollar_value.sum()
