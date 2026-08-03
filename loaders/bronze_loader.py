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
    def _save_json(destination, data):

        destination.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(destination, "w", encoding="utf-8") as f:

            # Lists → JSON Lines (NDJSON)
            if isinstance(data, list):

                for record in data:
                    f.write(
                        json.dumps(
                            record,
                            ensure_ascii=False
                        )
                    )
                    f.write("\n")

            # Single object → Normal JSON
            else:

                json.dump(
                    data,
                    f,
                    indent=4,
                    ensure_ascii=False
                )

        print(f"Saved: {destination}")

    @staticmethod
    def save_channel(data):

        partition = get_partition_path(BRONZE_CHANNEL_DIR)

        destination = partition / "channel.json"

        BronzeLoader._save_json(
            destination,
            data
        )

    @staticmethod
    def save_videos(data):

        partition = get_partition_path(BRONZE_VIDEOS_DIR)

        destination = partition / "videos.json"

        BronzeLoader._save_json(
            destination,
            data
        )

    @staticmethod
    def save_video_statistics(data):

        partition = get_partition_path(
            BRONZE_VIDEO_STATISTICS_DIR
        )

        destination = partition / "video_statistics.json"

        BronzeLoader._save_json(
            destination,
            data
        )

    @staticmethod
    def save_metadata(data):

        partition = get_partition_path(BRONZE_METADATA_DIR)

        destination = partition / "metadata.json"

        BronzeLoader._save_json(
            destination,
            data
        )