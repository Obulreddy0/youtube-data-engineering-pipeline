import pandas as pd

print("=" * 50)
print("DIM CHANNEL")
print("=" * 50)

df = pd.read_parquet("data/gold/dimensions/dim_channel.parquet")
print(df.shape)
print(df)

print("\n" + "=" * 50)
print("DIM VIDEO")
print("=" * 50)

df = pd.read_parquet("data/gold/dimensions/dim_video.parquet")
print(df.shape)
print(df.head())

print("\n" + "=" * 50)
print("DIM DATE")
print("=" * 50)

df = pd.read_parquet("data/gold/dimensions/dim_date.parquet")
print(df.shape)
print(df.head())