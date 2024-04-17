import pandas as pd

df = pd.read_csv("train.csv")
df[:150].to_csv("train_1.csv")
df[150:].to_csv("val_1.csv")