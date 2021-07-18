df_cancer = pd.DataFrame(np.c_[cancer['data'], cancer['target']], columns = np.append(cancer['feature_names'], ['target']))

# OR...
df_cancer = pd.read_csv('breast_cancer_cell_data.csv')
