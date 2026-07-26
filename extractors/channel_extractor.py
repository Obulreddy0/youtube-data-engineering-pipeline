import json
import os

from clients.youtube_client import YouTubeClient
from config.settings import CHANNEL_HANDLE


class ChannelExtractor:

    def __init__(self):
        self.youtube = YouTubeClient.get_client()

    def get_channel_details(self):

        response = self.youtube.channels().list(
            part="snippet,statistics,contentDetails",
            forHandle=CHANNEL_HANDLE.replace("@", "")
        ).execute()

        if not response["items"]:
            raise Exception(
                f"Channel not found: {CHANNEL_HANDLE}"
            )

        channel = response["items"][0]

        os.makedirs("data/bronze", exist_ok=True)

        with open(
            "data/bronze/channel.json",
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(
                channel,
                f,
                indent=4,
                ensure_ascii=False
            )

        return channel