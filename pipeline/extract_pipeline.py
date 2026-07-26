from extractors.channel_extractor import ChannelExtractor
from extractors.video_extractor import VideoExtractor
from extractors.statistics_extractor import StatisticsExtractor


class ExtractPipeline:

    def run(self):

        print("=" * 60)
        print("STARTING EXTRACT PIPELINE")
        print("=" * 60)

        channel = ChannelExtractor().get_channel_details()

        uploads_playlist = (
            channel["contentDetails"]
                  ["relatedPlaylists"]
                  ["uploads"]
        )

        videos = VideoExtractor().get_all_videos(
            uploads_playlist
        )

        video_ids = [
            video["contentDetails"]["videoId"]
            for video in videos
        ]

        StatisticsExtractor().get_video_statistics(
            video_ids
        )

        print("\nEXTRACT PIPELINE COMPLETED\n")