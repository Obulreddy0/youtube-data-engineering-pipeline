import json
import os

import pandas as pd

from config.constants import (
    BRONZE_DIR,
    SILVER_DIR,
    CHANNEL_FILE,
    VIDEOS_FILE,
    VIDEO_STATS_FILE
)


class BronzeToSilverTransformer:

    def __init__(self):

        os.makedirs(SILVER_DIR, exist_ok=True)

    def transform_channel(self):

        with open(
            os.path.join(BRONZE_DIR, CHANNEL_FILE),
            encoding="utf-8"
        ) as file:

            channel = json.load(file)

        data = {
            "channel_id": channel["id"],
            "title": channel["snippet"]["title"],
            "description": channel["snippet"]["description"],
            "country": channel["snippet"].get("country"),
            "published_at": channel["snippet"]["publishedAt"],
            "subscriber_count": int(channel["statistics"]["subscriberCount"]),
            "video_count": int(channel["statistics"]["videoCount"]),
            "view_count": int(channel["statistics"]["viewCount"])
        }

        df = pd.DataFrame([data])

        df.to_parquet(
            os.path.join(SILVER_DIR, "channel.parquet"),
            index=False
        )

        print("✅ channel.parquet created")

    def transform_videos(self):

        with open(
            os.path.join(BRONZE_DIR, VIDEOS_FILE),
            encoding="utf-8"
        ) as file:

            videos = json.load(file)

        rows = []

        for video in videos:

            rows.append({

                "video_id":
                    video["contentDetails"]["videoId"],

                "title":
                    video["snippet"]["title"],

                "published_at":
                    video["snippet"]["publishedAt"],

                "playlist_position":
                    video["snippet"]["position"]

            })

        df = pd.DataFrame(rows)

        df.to_parquet(
            os.path.join(SILVER_DIR, "videos.parquet"),
            index=False
        )

        print("✅ videos.parquet created")

    def transform_statistics(self):

        with open(
            os.path.join(BRONZE_DIR, VIDEO_STATS_FILE),
            encoding="utf-8"
        ) as file:

            stats = json.load(file)

        rows = []

        for video in stats:

            statistics = video.get("statistics", {})
            snippet = video.get("snippet", {})
            content = video.get("contentDetails", {})

            rows.append({

                "video_id":
                    video["id"],

                "title":
                    snippet.get("title"),

                "published_at":
                    snippet.get("publishedAt"),

                "view_count":
                    int(statistics.get("viewCount", 0)),

                "like_count":
                    int(statistics.get("likeCount", 0)),

                "comment_count":
                    int(statistics.get("commentCount", 0)),

                "duration":
                    content.get("duration")

            })

        df = pd.DataFrame(rows)

        df.to_parquet(
            os.path.join(
                SILVER_DIR,
                "video_statistics.parquet"
            ),
            index=False
        )

        print("✅ video_statistics.parquet created")