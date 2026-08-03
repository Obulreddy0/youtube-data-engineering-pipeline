import json
import pandas as pd

from loaders.silver_loader import SilverLoader

from config.paths import (
    BRONZE_CHANNEL_FILE,
    BRONZE_VIDEOS_FILE,
    BRONZE_VIDEO_STATISTICS_FILE
)


class BronzeToSilverTransformer:

    def transform(self):

        self._transform_channel()
        self._transform_videos()
        self._transform_statistics()

        print("\n✅ Bronze → Silver Transformation Completed Successfully")

    # ---------------------------------------------------
    # Channel
    # ---------------------------------------------------

    def _transform_channel(self):

        with open(BRONZE_CHANNEL_FILE, "r", encoding="utf-8") as f:
            channel = json.load(f)

        row = {
            "channel_id": channel["id"],
            "channel_title": channel["snippet"]["title"],
            "description": channel["snippet"]["description"],
            "country": channel["snippet"].get("country"),
            "published_at": channel["snippet"]["publishedAt"],
            "subscriber_count": int(channel["statistics"]["subscriberCount"]),
            "view_count": int(channel["statistics"]["viewCount"]),
            "video_count": int(channel["statistics"]["videoCount"])
        }

        df = pd.DataFrame([row])

        SilverLoader.save_channel(df)

        print("✔ Channel transformed")

    # ---------------------------------------------------
    # Videos
    # ---------------------------------------------------

    def _transform_videos(self):

        with open(BRONZE_VIDEOS_FILE, "r", encoding="utf-8") as f:
            videos = [json.loads(line) for line in f if line.strip()]

        rows = []

        for video in videos:

            rows.append({
                "video_id": video["contentDetails"]["videoId"],
                "channel_id": video["snippet"]["channelId"],
                "title": video["snippet"]["title"],
                "description": video["snippet"]["description"],
                "published_at": video["contentDetails"]["videoPublishedAt"],
                "thumbnail_url": video["snippet"]["thumbnails"]["high"]["url"]
            })

        df = pd.DataFrame(rows)

        SilverLoader.save_videos(df)

        print("✔ Videos transformed")

    # ---------------------------------------------------
    # Video Statistics
    # ---------------------------------------------------

    def _transform_statistics(self):

        with open(BRONZE_VIDEO_STATISTICS_FILE, "r", encoding="utf-8") as f:
            statistics = [json.loads(line) for line in f if line.strip()]

        rows = []

        for item in statistics:

            rows.append({
                "video_id": item["id"],
                "view_count": int(item["statistics"].get("viewCount", 0)),
                "like_count": int(item["statistics"].get("likeCount", 0)),
                "comment_count": int(item["statistics"].get("commentCount", 0)),
                "duration": item["contentDetails"]["duration"]
            })

        df = pd.DataFrame(rows)

        SilverLoader.save_video_statistics(df)

        print("✔ Video statistics transformed")