from extractors.channel_extractor import ChannelExtractor
from extractors.video_extractor import VideoExtractor
from extractors.statistics_extractor import StatisticsExtractor


def main():

    # Step 1
    channel = ChannelExtractor().get_channel_details()

    uploads_playlist = channel["contentDetails"]["relatedPlaylists"]["uploads"]

    # Step 2
    videos = VideoExtractor().get_all_videos(
        uploads_playlist
    )

    print(f"\nVideos Extracted : {len(videos)}")

    # Step 3
    video_ids = [
        video["contentDetails"]["videoId"]
        for video in videos
    ]

    # Step 4
    stats = StatisticsExtractor().get_video_statistics(
        video_ids
    )

    print(f"\nStatistics Extracted : {len(stats)}")


if __name__ == "__main__":
    main()