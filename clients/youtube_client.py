from googleapiclient.discovery import build
from config.settings import get_youtube_api_key


class YouTubeClient:

    @staticmethod
    def get_client():
        return build(
            serviceName="youtube",
            version="v3",
            developerKey=get_youtube_api_key()
        )