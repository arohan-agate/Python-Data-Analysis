# Plot scatter plot between mean area and mean smoothness
plt.figure(figsize = (10,10))

sns.scatterplot(x = 'mean area', y = 'mean smoothness', data = df_cancer, hue = 'target')
