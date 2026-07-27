import pandas as pd

df = pd.read_parquet("data/silver/video_statistics.parquet")

print(df.head())
print(df.info())