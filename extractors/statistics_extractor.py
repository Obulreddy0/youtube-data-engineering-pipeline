from clients.youtube_client import YouTubeClient
from loaders.bronze_loader import BronzeLoader
from config.constants import (
    BRONZE_DIR,
    VIDEO_STATS_FILE
)


class StatisticsExtractor:

    def __init__(self):
        self.youtube = YouTubeClient.get_client()

    def get_video_statistics(self, video_ids):

        statistics = []

        for i in range(0, len(video_ids), 50):

            batch = video_ids[i:i + 50]

            request = self.youtube.videos().list(
                part="snippet,statistics,contentDetails",
                id=",".join(batch)
            )

            response = request.execute()

            statistics.extend(response["items"])

            print(
                f"Processed {min(i + 50, len(video_ids))}/{len(video_ids)} videos"
            )

        BronzeLoader.save_json(
            statistics,
            BRONZE_DIR,
            VIDEO_STATS_FILE
        )

        return statistics