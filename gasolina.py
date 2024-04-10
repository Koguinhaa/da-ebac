import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

gasolina_df = pd.read_csv('gasolina.csv')
sns.relplot(data=gasolina_df, kind='line', x='dia', y='venda')
plt.savefig('gasolina.png')