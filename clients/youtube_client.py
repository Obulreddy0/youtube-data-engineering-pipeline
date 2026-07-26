from googleapiclient.discovery import build
from config.settings import YOUTUBE_API_KEY


class YouTubeClient:

    @staticmethod
    def get_client():
        return build(
            serviceName="youtube",
            version="v3",
            developerKey=YOUTUBE_API_KEY
        )