import json
import os

from clients.youtube_client import YouTubeClient


class StatisticsExtractor:

    def __init__(self):
        self.youtube = YouTubeClient.get_client()

    def get_video_statistics(self, video_ids):

        statistics = []

        # Process 50 video IDs at a time (YouTube API limit)
        for i in range(0, len(video_ids), 50):

            batch = video_ids[i:i + 50]

            request = self.youtube.videos().list(
                part="snippet,statistics,contentDetails",
                id=",".join(batch)
            )

            response = request.execute()

            statistics.extend(response["items"])

            print(f"Processed {min(i + 50, len(video_ids))}/{len(video_ids)} videos")

        os.makedirs("data/bronze", exist_ok=True)

        with open(
            "data/bronze/video_statistics.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                statistics,
                file,
                indent=4,
                ensure_ascii=False
            )

        return statistics