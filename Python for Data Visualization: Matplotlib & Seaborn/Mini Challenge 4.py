mu = daily_return_df['TWTR'].mean()
sigma = daily_return_df['TWTR'].std()

num_bins = 30
plt.figure(figsize = (10, 10))
plt.hist(daily_return_df['TWTR'], num_bins, facecolor = 'c')
plt.grid()

plt.title('Histogram: mu = ' + str(mu) + ", sigma = " + str(sigma))
