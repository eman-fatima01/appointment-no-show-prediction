import pandas as pd

df = pd.read_csv("data/KaggleV2-May-2016.csv")
df = df[(df["Age"] >= 0) & (df["Age"] <= 100)]

df["ScheduledDay"] = pd.to_datetime(df["ScheduledDay"])
df["AppointmentDay"] = pd.to_datetime(df["AppointmentDay"])
print(df[["ScheduledDay", "AppointmentDay"]].dtypes)

scheduled = (df["ScheduledDay"].dt.normalize())
df["waiting_days"] = (df["AppointmentDay"] - scheduled).dt.days
print(df["waiting_days"].describe())

negative = df["waiting_days" ] < 0
print(negative.sum())

df = df[(df["waiting_days"] >= 0)]
print(df.shape)