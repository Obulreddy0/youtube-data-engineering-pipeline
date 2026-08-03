import pandas as pd

from utils.date_partition import get_partition_path

from config.paths import (
    SILVER_CHANNEL_DIR,
    SILVER_VIDEOS_DIR,
    SILVER_VIDEO_STATISTICS_DIR
)


class SilverLoader:

    @staticmethod
    def save_channel(df: pd.DataFrame):

        partition = get_partition_path(SILVER_CHANNEL_DIR)
        partition.mkdir(parents=True, exist_ok=True)

        destination = partition / "channel.parquet"

        df.to_parquet(
            destination,
            index=False
        )

        print(f"Saved: {destination}")

    @staticmethod
    def save_videos(df: pd.DataFrame):

        partition = get_partition_path(SILVER_VIDEOS_DIR)
        partition.mkdir(parents=True, exist_ok=True)

        destination = partition / "videos.parquet"

        df.to_parquet(
            destination,
            index=False
        )

        print(f"Saved: {destination}")

    @staticmethod
    def save_video_statistics(df: pd.DataFrame):

        partition = get_partition_path(
            SILVER_VIDEO_STATISTICS_DIR
        )
        partition.mkdir(parents=True, exist_ok=True)

        destination = (
            partition / "video_statistics.parquet"
        )

        df.to_parquet(
            destination,
            index=False
        )

        print(f"Saved: {destination}")