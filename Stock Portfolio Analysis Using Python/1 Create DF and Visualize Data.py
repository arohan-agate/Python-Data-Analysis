# Open, read, and display the CSV file with the stock data
stocks_df = pd.read_csv('stock_data.csv')
display(stocks_df)

# Function to plot interactive graph
def i_plot(df, title):
    fig = px.line(title = title)
    for i in df.columns[1:]:
        fig.add_scatter(x = df['Date'], y = df[i], name = i)
    fig.show()

# Plot interactive graph
i_plot(stocks_df, 'Stock Prices')

# Plot normalized graph of stock prices (scaled to where the initial prices are all the same)
def normalize(df):
    x = df.copy()
    for i in x.columns[1:]:
        x[i] = x[i]/x[i][0]
    return x

# Display the interactive graph of normalized data
i_plot(normalize(stocks_df), 'Normalized Stock Prices')
