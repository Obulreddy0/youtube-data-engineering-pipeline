from googleapiclient.discovery import build
from config.settings import YOUTUBE_API_KEY


def get_youtube_client():
    """
    Creates and returns an authenticated YouTube API client.
    """

    youtube = build(
        serviceName="youtube",
        version="v3",
        developerKey=YOUTUBE_API_KEY
    )

    return youtube