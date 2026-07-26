import json
import os
import time

from googleapiclient.errors import HttpError

from clients.youtube_client import YouTubeClient


class VideoExtractor:

    def __init__(self):
        self.youtube = YouTubeClient.get_client()

    def get_all_videos(self, uploads_playlist_id):

        videos = []
        next_page_token = None

        while True:

            request = self.youtube.playlistItems().list(
                part="snippet,contentDetails",
                playlistId=uploads_playlist_id,
                maxResults=50,
                pageToken=next_page_token
            )

            max_retries = 3

            for attempt in range(max_retries):

                try:
                    response = request.execute()
                    break

                except (ConnectionResetError, HttpError) as e:

                    print(f"\nRetry {attempt + 1}/{max_retries}")
                    print(e)

                    time.sleep(3)

                    if attempt == max_retries - 1:
                        raise

            videos.extend(response["items"])

            print(f"Downloaded {len(videos)} videos...")

            next_page_token = response.get("nextPageToken")

            if not next_page_token:
                break

        os.makedirs("data/bronze", exist_ok=True)

        with open(
            "data/bronze/videos.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                videos,
                file,
                indent=4,
                ensure_ascii=False
            )

        return videos