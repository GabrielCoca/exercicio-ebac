import pandas as pd
import seaborn as sns

df = pd.read_csv('gasolina.csv')
sns.lineplot(x='dia', y='venda', data=df)
