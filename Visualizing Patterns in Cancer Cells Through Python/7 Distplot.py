# distplot between benign and malignant cells, displays distribution and average radius

class_0_df = df_cancer[df_cancer['target'] == 0]
class_1_df = df_cancer[df_cancer['target'] == 1]

plt.figure(figsize = (10, 7))
sns.distplot(class_0_df['mean radius'], bins = 25, color = 'b')
sns.distplot(class_1_df['mean radius'], bins = 25, color = 'r')
plt.grid()
