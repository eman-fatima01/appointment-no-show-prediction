import pandas as pd
df = pd.read_csv("data/KaggleV2-May-2016.csv")
print(df.shape)
print(df.head())
print(df.info())
print(df["No-show"].value_counts())