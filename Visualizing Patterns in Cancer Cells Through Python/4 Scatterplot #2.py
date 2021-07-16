# plots scatterplot between the mean radius and mean area

plt.figure(figsize = (10,10))
sns.scatterplot(x = 'mean radius', y = 'mean area', data = df_cancer, hue = 'target')
