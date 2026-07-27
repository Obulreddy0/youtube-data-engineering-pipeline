import pandas as pd

from config.paths import SILVER_PARTITION


class SilverLoader:

    @staticmethod
    def save_parquet(df, file_path):

        destination = SILVER_PARTITION / file_path.name

        df.to_parquet(
            destination,
            index=False
        )

        print(f"Saved: {destination}")