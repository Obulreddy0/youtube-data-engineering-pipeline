from pathlib import Path
import pandas as pd

from config.paths import get_silver_partition


class SilverLoader:

    @staticmethod
    def save_parquet(df: pd.DataFrame, file_path: Path):

        partition = get_silver_partition()

        destination = partition / file_path.name

        df.to_parquet(
            destination,
            index=False
        )

        print(f"Saved: {destination}")