import pandas as pd
df = pd.read_csv("data/KaggleV2-May-2016.csv")
print(df.shape)
print(df.head())
print(df.info())
print(df["No-show"].value_counts())
print(df["Age"].describe())
print(df["Gender"].value_counts())
print((df["Age"] < 0).sum())
print((df["Age"] > 100).sum())
df = df[(df["Age"] >= 0) & (df["Age"] <= 100)]
print(df.shape)