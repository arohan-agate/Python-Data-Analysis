# Step 1:
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns

EPL_start = pd.read_excel('Assignment Data/Week 1/EPL2017-18.xlsx')
print(EPL_start.columns.tolist())


# Step 2:
EPL = EPL_start[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']]
EPL = EPL.rename(columns={'FTR':'Result'})
EPL


# Step 3:
EPL['hwinvalue']=np.where(EPL['Result']=='H',1,np.where(EPL['Result']=='D',.5,0))
EPL['awinvalue']=np.where(EPL['Result']=='A',1,np.where(EPL['Result']=='D',.5,0))
EPL['count']=1
EPL


# Step 4:
EPL17 = EPL[EPL.Date < 20180000]

EPL17_Home = EPL17.groupby('HomeTeam')['count','hwinvalue', 'FTHG','FTAG'].sum().reset_index()
EPL17_Home = EPL17_Home.rename(columns={'HomeTeam':'team', 'count':'GP_h', 'FTHG':'FTHGh','FTAG':'FTAGh'})
EPL17_Home


# Step 5:
EPL17_Away = EPL17.groupby('AwayTeam')['count','awinvalue', 'FTHG','FTAG'].sum().reset_index()
EPL17_Away = EPL17_Away.rename(columns={'AwayTeam':'team','count':'GP_a','FTHG':'FTHGa','FTAG':'FTAGa'})
EPL17_Away


# Step 6:
EPL17 = pd.merge(EPL17_Home, EPL17_Away, on = ['team'])
EPL17['W'] = EPL17['hwinvalue']+EPL17['awinvalue']
EPL17['G'] = EPL17['GP_h']+EPL17['GP_a']
EPL17['GoalsFor'] = EPL17['FTHGh']+EPL17['FTAGa']
EPL17['GoalsAgainst'] = EPL17['FTAGh']+EPL17['FTHGa']
EPL17['wpc17'] = EPL17['W']/EPL17['G']
EPL17['pyth17'] = EPL17['GoalsFor']**2/(EPL17['GoalsFor']**2 + EPL17['GoalsAgainst']**2)
EPL17


# Step 7a:
EPL18 = EPL[EPL.Date > 20180000]

EPL18_Home = EPL18.groupby('HomeTeam')['count','hwinvalue', 'FTHG','FTAG'].sum().reset_index()
EPL18_Home = EPL18_Home.rename(columns={'HomeTeam':'team', 'count':'GP_h', 'FTHG':'FTHGh','FTAG':'FTAGh'})
EPL18_Home


# Step 7b:
EPL18_Away = EPL18.groupby('AwayTeam')['count','awinvalue', 'FTHG','FTAG'].sum().reset_index()
EPL18_Away = EPL18_Away.rename(columns={'AwayTeam':'team','count':'GP_a','FTHG':'FTHGa','FTAG':'FTAGa'})
EPL18_Away


Step 7c:
EPL18 = pd.merge(EPL18_Home, EPL18_Away, on = ['team'])
EPL18['W'] = EPL18['hwinvalue']+EPL18['awinvalue']
EPL18['G'] = EPL18['GP_h']+EPL18['GP_a']
EPL18['GoalsFor'] = EPL18['FTHGh']+EPL18['FTAGa']
EPL18['GoalsAgainst'] = EPL18['FTAGh']+EPL18['FTHGa']
EPL18['wpc18'] = EPL18['W']/EPL18['G']
EPL18['pyth18'] = EPL18['GoalsFor']**2/(EPL18['GoalsFor']**2 + EPL18['GoalsAgainst']**2)
EPL18


Step 8:
merged = pd.merge(EPL17, EPL18, on="team")
merged


Step 9:
keyvars = merged[['team','wpc18','wpc17','pyth18','pyth17']]
keyvars.corr()
