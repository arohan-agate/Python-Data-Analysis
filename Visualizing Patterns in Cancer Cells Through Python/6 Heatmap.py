# Strong correlation between the mean radius and mean perimeter, mean area and mean primeter

plt.figure(figsize = (30, 30)) 
sns.heatmap(df_cancer.corr(), annot = True)
