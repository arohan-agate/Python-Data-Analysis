plt.figure(figsize = (17, 17))

plt.subplot(3, 1, 1)  # 1 row, 2 columns. specifies that this will be in the first column
plt.plot(stock_df['NFLX'], 'r--')
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(stock_df['FB'], 'b.')
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(stock_df['TWTR'], 'c--')
plt.grid()
