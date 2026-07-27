from extractors.channel_extractor import ChannelExtractor
from extractors.video_extractor import VideoExtractor
from extractors.statistics_extractor import StatisticsExtractor


class ExtractPipeline:

    def run(self):

        print("=" * 60)
        print("STARTING EXTRACT PIPELINE")
        print("=" * 60)

        # Step 1: Extract channel details
        channel = ChannelExtractor().get_channel_details()

        uploads_playlist = (
            channel["contentDetails"]["relatedPlaylists"]["uploads"]
        )

        # Step 2: Extract videos
        video_extractor = VideoExtractor()

        videos = video_extractor.get_all_videos(
            uploads_playlist
        )

        # Step 3: Collect all video IDs
        video_ids = [
            video["contentDetails"]["videoId"]
            for video in videos
        ]

        # Step 4: Extract statistics
        statistics_extractor = StatisticsExtractor()

        statistics_extractor.get_video_statistics(
            video_ids
        )

        print("=" * 60)
        print("EXTRACT PIPELINE COMPLETED")
        print("=" * 60)