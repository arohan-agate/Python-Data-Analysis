# Plotting GDP vs. number of max infections
x1 = df['GDP per capita']
y1 = df['max infection rate']
sns.regplot(x1, np.log(y1))

# Plotting Social support vs. number of max infections
x2 = df['Social support']
y2 = df['max infection rate']
sns.regplot(x2, np.log(y2))

# Plotting Healthy life expectancy vs. number of max infections
x3 = df['Healthy life expectancy']
y3 = df['max infection rate']
sns.regplot(x3, np.log(y3))

# Plotting Freedom to make life choices vs. number of max infections
x4 = df['Freedom to make life choices']
y4 = df['max infection rate']
sns.regplot(x4, np.log(y4))
