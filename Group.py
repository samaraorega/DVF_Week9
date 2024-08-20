#.groupby() method aggregates different groups in a data frame

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("titanic.csv")
df.groupby('Sex').sum() #Prints out the total of both genders and the sum of the numerical columns

#To inspect available methods
grouped_df = df.groupby('Sex')
#grouped_df.<TAB>

#Can also be done for multiple groups
df.groupby(['Sex', 'Pclass']).mean()

#You can also slice a selection of columns you're interested in
df.groupby(['Sex', 'Pclass'])['Survived'].mean()
#This only returns the mean in the Survived column