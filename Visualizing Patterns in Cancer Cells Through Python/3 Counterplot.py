# prints out countplot to know how many samples belong to class #0 and #1
plt.figure(figsize = (10,10))
sns.countplot(df_cancer['target'], label = "Count")
