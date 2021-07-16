values = [20, 20, 20, 20, 20]
colors = ['g', 'r', 'y', 'b', 'm']
labels = ['AAPL', 'GOOG', 'T', 'TSLA', 'AMZN']
explode = [0, 0.2, 0, 0, 0.2]

# Use matplotlib to plot a pie chart 
plt.figure(figsize = (10, 10))
plt.pie(values, colors = colors, labels = labels, explode = explode)
plt.title('STOCK PORTFOLIO')
