import pandas as pd
df = pd.read_csv("data/clean.csv")
print(df.shape)
print(df["target"].mean())
print(df.groupby("SMS_received")["target"].mean())
print(df.groupby("SMS_received")["waiting_days"].mean())
print(df.groupby("SMS_received")["waiting_days"].min())
df["wait_group"] = pd.cut(df["waiting_days"], bins=[-1, 0, 3, 7, 14, 30, 200], labels=["same day", "1-3", "4-7", "8-14", "15-30", "30+"])
print(df.groupby("wait_group")["target"].mean())