import os

from clients.youtube_client import YouTubeClient
from config.settings import CHANNEL_HANDLE
from loaders.bronze_loader import BronzeLoader
from config.constants import BRONZE_DIR, CHANNEL_FILE


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

        BronzeLoader.save_json(
            channel,
            BRONZE_DIR,
            CHANNEL_FILE
        )

        return channel