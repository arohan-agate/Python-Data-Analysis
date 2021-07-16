fig = plt.figure(figsize = (15, 15))
ax = fig.add_subplot(111, projection = '3d')

x = daily_return_df['TWTR'].tolist()
y = daily_return_df['FB'].tolist()
z = daily_return_df['NFLX'].tolist()

ax.scatter(x, y, z, c = 'r', s = 1000)
ax.set_xlabel('TWTR label')
ax.set_ylabel('FB label')
ax.set_zlabel('NFLX label')
