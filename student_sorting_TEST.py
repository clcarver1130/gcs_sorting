# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read in data
df = pd.read_csv('renweb_TEST.csv')

# Group by Family and find Largest Grade Value per Family Group
release_dict = df.groupby(['Parents'], sort=False)['Grade'].max().to_dict()

# Assign New 'Release Grade' value to each Student
df['Release Grade'] = df['Parents'].map(release_dict)

# Group by 'Release Grade' and create visual
df.groupby('Release Grade').count()['Student'].plot(kind='bar')
plt.show()
