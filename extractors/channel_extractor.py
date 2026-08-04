from clients.youtube_client import YouTubeClient
from loaders.bronze_loader import BronzeLoader
from config.settings import get_channel_handle


class ChannelExtractor:

    def __init__(self):
        self.youtube = YouTubeClient.get_client()

    def get_channel_details(self):

        response = self.youtube.channels().list(
            part="snippet,statistics,contentDetails",
            forHandle=get_channel_handle().replace("@", "")
        ).execute()

        if not response["items"]:
            raise Exception(f"Channel not found: {get_channel_handle()}")

        channel = response["items"][0]

        BronzeLoader.save_channel(channel)

        print("✅ Channel extracted successfully.")

        return channel