import pandas as pd


class GoldLoader:

    @staticmethod
    def save_parquet(df, file_path):

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        df.to_parquet(
            file_path,
            index=False
        )

        print(f"Saved: {file_path}")