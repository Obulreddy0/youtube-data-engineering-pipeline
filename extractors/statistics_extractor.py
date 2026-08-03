import time

from googleapiclient.errors import HttpError

from clients.youtube_client import YouTubeClient
from loaders.bronze_loader import BronzeLoader


class VideoStatisticsExtractor:

    def __init__(self):
        self.youtube = YouTubeClient.get_client()

    def get_video_statistics(self, videos):

        statistics = []

        video_ids = [
            video["contentDetails"]["videoId"]
            for video in videos
        ]

        batch_size = 50

        for i in range(0, len(video_ids), batch_size):

            batch = video_ids[i:i + batch_size]

            max_retries = 3

            for attempt in range(max_retries):

                try:
                    response = self.youtube.videos().list(
                        part="snippet,contentDetails,statistics",
                        id=",".join(batch)
                    ).execute()

                    break

                except (ConnectionResetError, HttpError) as e:

                    print(f"Retry {attempt + 1}/{max_retries}")
                    print(e)

                    time.sleep(3)

                    if attempt == max_retries - 1:
                        raise

            statistics.extend(response["items"])

            print(
                f"Processed {min(i + batch_size, len(video_ids))}/{len(video_ids)} videos"
            )

        BronzeLoader.save_video_statistics(statistics)

        print("✅ Video statistics extracted successfully.")

        return statistics