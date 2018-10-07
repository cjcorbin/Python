import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np
from sklearn.cluster import KMeans
import csv

df = pd.read_csv('kmeans.csv')


kmeans = KMeans(n_clusters=3, random_state=0).fit(df)
labels = kmeans.labels_
df_labels = pd.DataFrame(labels)
df_labels.columns = ['classes']

dat1 = pd.concat([df, df_labels], axis=1)

colors = ['red','green','blue']

scatter_matrix(dat1, figsize=[6,6],  diagonal='kde', marker='o', c=dat1.classes.apply(lambda x:colors[x]))

plt.show()
