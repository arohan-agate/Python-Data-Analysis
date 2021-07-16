# relationship between benign and malignant cells when it comes to radius, texture, area, perimeter, and smoothness

sns.pairplot(df_cancer, hue = 'target', vars = ['mean radius', 'mean texture', 'mean area', 'mean perimeter', 'mean smoothness'])
