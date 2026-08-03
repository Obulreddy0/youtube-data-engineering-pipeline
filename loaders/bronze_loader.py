import json

from config.paths import (
    BRONZE_CHANNEL_DIR,
    BRONZE_VIDEOS_DIR,
    BRONZE_VIDEO_STATISTICS_DIR,
    BRONZE_METADATA_DIR,
)

from utils.date_partition import get_partition_path


class BronzeLoader:

    @staticmethod
    def save_channel(data):

        partition = get_partition_path(BRONZE_CHANNEL_DIR)
        partition.mkdir(parents=True, exist_ok=True)

        destination = partition / "channel.json"

        with open(destination, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(f"Saved: {destination}")

    @staticmethod
    def save_videos(data):

        partition = get_partition_path(BRONZE_VIDEOS_DIR)
        partition.mkdir(parents=True, exist_ok=True)

        destination = partition / "videos.json"

        with open(destination, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(f"Saved: {destination}")

    @staticmethod
    def save_video_statistics(data):

        partition = get_partition_path(BRONZE_VIDEO_STATISTICS_DIR)
        partition.mkdir(parents=True, exist_ok=True)

        destination = partition / "video_statistics.json"

        with open(destination, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(f"Saved: {destination}")

    @staticmethod
    def save_metadata(data):

        partition = get_partition_path(BRONZE_METADATA_DIR)
        partition.mkdir(parents=True, exist_ok=True)

        destination = partition / "metadata.json"

        with open(destination, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(f"Saved: {destination}")