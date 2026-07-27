import json
import pandas as pd

from loaders.silver_loader import SilverLoader

from config.paths import (
    get_bronze_partition,
    SILVER_CHANNEL_FILE,
    SILVER_VIDEOS_FILE,
    SILVER_VIDEO_STATISTICS_FILE
)


class BronzeToSilverTransformer:

    def transform(self):

        print("=" * 60)
        print("STARTING TRANSFORM PIPELINE")
        print("=" * 60)

        self._transform_channel()
        self._transform_videos()
        self._transform_statistics()

        print("\n✅ Bronze → Silver Transformation Completed Successfully")
        print("=" * 60)
        print("TRANSFORM PIPELINE COMPLETED")
        print("=" * 60)

    # =====================================================
    # Channel
    # =====================================================

    def _transform_channel(self):

        bronze_partition = get_bronze_partition()

        with open(
            bronze_partition / "channel.json",
            "r",
            encoding="utf-8"
        ) as f:

            channel = json.load(f)

        row = {

            "channel_id": channel["id"],

            "channel_title": channel["snippet"]["title"],

            "description": channel["snippet"]["description"],

            "country": channel["snippet"].get("country"),

            "published_at": channel["snippet"]["publishedAt"],

            "subscriber_count": int(
                channel["statistics"]["subscriberCount"]
            ),

            "view_count": int(
                channel["statistics"]["viewCount"]
            ),

            "video_count": int(
                channel["statistics"]["videoCount"]
            )

        }

        df = pd.DataFrame([row])

        SilverLoader.save_parquet(
            df,
            SILVER_CHANNEL_FILE
        )

        print("✔ Channel transformed")

    # =====================================================
    # Videos
    # =====================================================

    def _transform_videos(self):

        bronze_partition = get_bronze_partition()

        with open(
            bronze_partition / "videos.json",
            "r",
            encoding="utf-8"
        ) as f:

            videos = json.load(f)

        rows = []

        for video in videos:

            rows.append({

                "video_id":
                    video["contentDetails"]["videoId"],

                "channel_id":
                    video["snippet"]["channelId"],

                "title":
                    video["snippet"]["title"],

                "description":
                    video["snippet"]["description"],

                "published_at":
                    video["contentDetails"]["videoPublishedAt"],

                "thumbnail_url":
                    video["snippet"]["thumbnails"]["high"]["url"]

            })

        df = pd.DataFrame(rows)

        SilverLoader.save_parquet(
            df,
            SILVER_VIDEOS_FILE
        )

        print("✔ Videos transformed")

    # =====================================================
    # Statistics
    # =====================================================

    def _transform_statistics(self):

        bronze_partition = get_bronze_partition()

        with open(
            bronze_partition / "video_statistics.json",
            "r",
            encoding="utf-8"
        ) as f:

            statistics = json.load(f)

        rows = []

        for item in statistics:

            rows.append({

                "video_id":
                    item["id"],

                "view_count":
                    int(item["statistics"].get("viewCount", 0)),

                "like_count":
                    int(item["statistics"].get("likeCount", 0)),

                "comment_count":
                    int(item["statistics"].get("commentCount", 0)),

                "duration":
                    item["contentDetails"]["duration"]

            })

        df = pd.DataFrame(rows)

        SilverLoader.save_parquet(
            df,
            SILVER_VIDEO_STATISTICS_FILE
        )

        print("✔ Video statistics transformed")